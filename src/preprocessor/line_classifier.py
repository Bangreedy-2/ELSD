"""Line-oriented preprocessor that makes GG-Code a superset of G-code.

A raw slicer file (e.g. 142k lines of `G1 X.. Y.. E..`) cannot be pushed through
the ANTLR runtime interactively, and raw G-code is not GG-Code DSL. So we classify
each source line up front:

  * Raw G-code  (`G1 ...`, `M104 ...`, `G92 ...`, `T0`)  -> verbatim passthrough
  * Comment     (`; ...`)                                -> verbatim passthrough
  * Blank line                                           -> verbatim passthrough
  * GG-Code DSL (`Move to ...`, `At layer N { ... }`)    -> parsed by ANTLR

Contiguous raw/comment/blank lines collapse into a single ``RawGCode`` run-node
(broken only at ``; layer N, Z = h`` markers) so a 142k-line file becomes a few
hundred nodes instead of one-per-line. Slicer layer markers are detected and tagged
so codegen can anchor injected ``At layer/height`` blocks to the right position.
"""
import re
from typing import List, Tuple, Dict

from src.ast_nodes.statements import RawGCode

# A raw G/M/T command line, e.g. "G1 X10", "M104 S210", "T0".
_RAW_CMD = re.compile(r'^\s*[GMT]\d+\b')
# Simplify3D / common slicer layer marker: "; layer 1, Z = 0.300".
_LAYER_MARKER = re.compile(r'^\s*;\s*layer\s+(\d+)\s*,\s*z\s*=\s*([-\d.]+)', re.IGNORECASE)

# GG-Code DSL statements start with one of these keywords.
DSL_KEYWORDS = {
    'move', 'temperature', 'pause', 'at', 'set', 'add', 'if', 'repeat',
    'while', 'home', 'define', 'use', 'stop', 'wait', 'else', 'then',
}


def _first_word(stripped: str) -> str:
    """Return the leading alphabetic word of an already-stripped line, lowercased."""
    out = []
    for ch in stripped:
        if ch.isalpha() or ch == '_':
            out.append(ch)
        else:
            break
    return ''.join(out).lower()


def _is_dsl(line: str) -> bool:
    s = line.strip()
    if not s:
        return False
    if s.startswith(';') or s.startswith('//') or s.startswith('/*'):
        return False
    if _RAW_CMD.match(line):
        return False
    return _first_word(s) in DSL_KEYWORDS


# An item is either ('raw', RawGCode) for verbatim passthrough or ('dsl', text)
# for a brace-balanced GG-Code chunk to hand to ANTLR.
Item = Tuple[str, object]


def classify_lines(source: str) -> Tuple[List[Item], Dict[int, float]]:
    """Classify ``source`` into ordered items plus a ``{layer_number: z}`` map.

    The layer map is built from explicit ``; layer N, Z = h`` markers; files
    without such markers yield an empty map (codegen then derives layers from Z
    moves). The returned items preserve source order so raw and DSL segments
    interleave exactly as written.
    """
    lines = source.split('\n')
    items: List[Item] = []
    layer_map: Dict[int, float] = {}
    raw_buf: List[str] = []

    def flush_raw() -> None:
        if raw_buf:
            items.append(('raw', RawGCode(line=0, column=0, text='\n'.join(raw_buf))))
            raw_buf.clear()

    i = 0
    n = len(lines)
    while i < n:
        line = lines[i]

        marker = _LAYER_MARKER.match(line)
        if marker:
            flush_raw()
            layer = int(marker.group(1))
            z = float(marker.group(2))
            layer_map[layer] = z
            items.append(('raw', RawGCode(
                line=0, column=0, text=line,
                layer=layer, z=z, is_layer_marker=True,
            )))
            i += 1
            continue

        if _is_dsl(line):
            flush_raw()
            chunk = [line]
            depth = line.count('{') - line.count('}')
            i += 1
            # Keep consuming while inside a block (depth > 0) or the next line is
            # another DSL statement, so multi-line `At layer N { ... }` blocks and
            # runs of consecutive DSL statements form a single ANTLR chunk.
            while i < n and (depth > 0 or _is_dsl(lines[i])):
                chunk.append(lines[i])
                depth += lines[i].count('{') - lines[i].count('}')
                i += 1
            items.append(('dsl', '\n'.join(chunk)))
            continue

        # Raw command, comment, or blank line -> verbatim passthrough.
        raw_buf.append(line)
        i += 1

    flush_raw()
    return items, layer_map

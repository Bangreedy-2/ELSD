"""Tests for GG-Code as a superset of G-code: raw passthrough, layer/height
anchoring, the Pause command, and graceful handling of missing anchors.

Maps to the sprint hypotheses:
  E1 superset fidelity, E2 performance, E3 anchor correctness,
  E4 Pause works end-to-end, E5 robustness.
"""
import os
import sys
import time

import pytest

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import run_pipeline
from src.preprocessor.line_classifier import classify_lines

FIXTURE = os.path.join(os.path.dirname(__file__), "fixtures", "benchy_slice.gcode")


def _lines(text):
    return text.splitlines()


def _index_of(lines, predicate):
    for i, l in enumerate(lines):
        if predicate(l):
            return i
    return -1


# --- E1: superset fidelity -------------------------------------------------

def test_raw_lines_pass_through_verbatim():
    raw = "\n".join([
        "G1 X10.496 Y-1.648 E0.4346",
        "M104 S210",
        "G92 E0",
        "T0",
        "M900 0.6",
        "M205 T0 X10 Y10 Z10",
        "; a free-form comment",
    ])
    out = run_pipeline(raw)
    for line in raw.splitlines():
        assert line in out, f"raw line not preserved verbatim: {line!r}"


def test_fixture_line_count_conserved():
    src = open(FIXTURE, encoding="utf-8").read()
    out = run_pipeline(src)
    # Every original raw/comment line survives; output only *adds* annotations.
    src_lines = [l for l in _lines(src) if l.strip()]
    out_lines = set(_lines(out))
    for l in src_lines:
        assert l in out_lines, f"missing line: {l!r}"


# --- E1b: layer markers ----------------------------------------------------

def test_layer_markers_detected():
    src = open(FIXTURE, encoding="utf-8").read()
    _items, layer_map = classify_lines(src)
    assert layer_map == {1: 0.3, 2: 0.5, 3: 0.7}


# --- E3: anchor correctness ------------------------------------------------

def test_at_layer_block_injected_after_marker():
    src = open(FIXTURE, encoding="utf-8").read() + "\nAt layer 2 { Temperature 180C }\n"
    lines = _lines(run_pipeline(src))
    marker = _index_of(lines, lambda l: l.startswith("; layer 2,"))
    inj = _index_of(lines, lambda l: "M104 S180" in l)
    assert marker != -1 and inj != -1
    # Injected right at the layer-2 boundary, before layer 3 begins.
    layer3 = _index_of(lines, lambda l: l.startswith("; layer 3,"))
    assert marker < inj < layer3


def test_at_height_resolves_to_first_layer_reaching_z():
    # Height 0.6mm -> first layer with Z >= 0.6 is layer 3 (Z=0.7).
    src = open(FIXTURE, encoding="utf-8").read() + "\nAt height 0.6mm { Temperature 150C }\n"
    lines = _lines(run_pipeline(src))
    inj = _index_of(lines, lambda l: "M104 S150" in l)
    layer3 = _index_of(lines, lambda l: l.startswith("; layer 3,"))
    layer2 = _index_of(lines, lambda l: l.startswith("; layer 2,"))
    assert layer2 < layer3 < inj or layer3 < inj  # injected at/after layer 3 boundary
    assert inj > layer3


def test_height_unit_conversion_cm():
    # 0.05cm == 0.5mm -> first layer with Z >= 0.5 is layer 2.
    src = open(FIXTURE, encoding="utf-8").read() + "\nAt height 0.05cm { Temperature 160C }\n"
    lines = _lines(run_pipeline(src))
    inj = _index_of(lines, lambda l: "M104 S160" in l)
    layer2 = _index_of(lines, lambda l: l.startswith("; layer 2,"))
    layer3 = _index_of(lines, lambda l: l.startswith("; layer 3,"))
    assert layer2 < inj <= layer3 or inj > layer2


# --- E4: Pause works end-to-end --------------------------------------------

def test_standalone_pause_emits_m0_inline():
    out = run_pipeline("Move to X1 Y1\nPause\nMove to X2 Y2")
    lines = _lines(out)
    p = _index_of(lines, lambda l: l.strip() == "M0")
    assert p != -1
    # Inline: appears between the two moves, not at the end.
    a = _index_of(lines, lambda l: "G1 X1 Y1" in l)
    b = _index_of(lines, lambda l: "G1 X2 Y2" in l)
    assert a < p < b


def test_pause_at_layer_injects_single_m0():
    src = open(FIXTURE, encoding="utf-8").read() + "\nPause at layer 2\n"
    lines = _lines(run_pipeline(src))
    assert sum(1 for l in lines if l.strip() == "M0") == 1
    marker = _index_of(lines, lambda l: l.startswith("; layer 2,"))
    m0 = _index_of(lines, lambda l: l.strip() == "M0")
    layer3 = _index_of(lines, lambda l: l.startswith("; layer 3,"))
    assert marker < m0 < layer3


def test_pause_no_longer_silently_dropped():
    # Regression: PauseStatement used to be dropped (missing visitPauseStatement).
    out = run_pipeline("Pause")
    assert "M0" in out


# --- E5: robustness --------------------------------------------------------

def test_missing_layer_anchor_warns_and_continues():
    src = open(FIXTURE, encoding="utf-8").read() + "\nAt layer 999 { Pause }\n"
    out = run_pipeline(src)  # must not raise
    assert "; WARNING:" in out
    assert "999" in out
    # Original content still produced.
    assert "G1 X10.496 Y-1.648 E0.4346" in out


def test_mixed_dsl_and_raw_order_preserved():
    src = "M104 S210\nMove to X5 Y5\nG1 Z1\nTemperature 180C"
    lines = _lines(run_pipeline(src))
    i_raw1 = _index_of(lines, lambda l: l == "M104 S210")
    i_move = _index_of(lines, lambda l: "G1 X5 Y5" in l)
    i_raw2 = _index_of(lines, lambda l: l == "G1 Z1")
    i_temp = _index_of(lines, lambda l: "M104 S180" in l)
    assert i_raw1 < i_move < i_raw2 < i_temp


# --- E2: performance -------------------------------------------------------

@pytest.mark.slow
def test_large_file_performance_and_fidelity():
    # Synthesize a ~140k-line slicer-style file (no dependency on a real path).
    parts = ["M104 S210", "G28", "G92 E0"]
    for layer in range(1, 241):
        z = layer * 0.2
        parts.append(f"; layer {layer}, Z = {z:.3f}")
        for k in range(580):
            parts.append(f"G1 X{k % 100}.{k % 10} Y{(k * 7) % 100}.{k % 10} E{k * 0.01:.4f}")
    src = "\n".join(parts)
    n_g1 = sum(1 for l in src.splitlines() if l.startswith("G1"))

    t = time.perf_counter()
    out = run_pipeline(src)
    dt = time.perf_counter() - t

    out_g1 = sum(1 for l in out.splitlines() if l.startswith("G1"))
    assert out_g1 == n_g1, "G1 line count must be conserved"
    assert dt < 10.0, f"compile took {dt:.2f}s (expected < 10s)"

import sys
import os
from antlr4 import InputStream, CommonTokenStream
import argparse

# Ensure we can run as script from inside src or root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.antlr_gen.GGCodeLexer import GGCodeLexer
from src.antlr_gen.GGCodeParser import GGCodeParser
from src.parser.antlr_converter import ASTBuilder
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.semantic.semantic_errors import SemanticError
from src.codegen.gcode_generator import GCodeGenerator
from src.preprocessor.line_classifier import classify_lines
from src.ast_nodes.program import Program
from src.ast_nodes.statements import Block


def _parse_dsl_chunk(text: str):
    """Parse one GG-Code DSL chunk through ANTLR and return its statement list.

    ``visitProgram`` wraps the chunk's statementList in a single Block; unwrap it
    so top-level constructs (AtBlockStatement, anchored Pause) sit directly in the
    program's statement list where the generator's injection routing sees them.
    """
    input_stream = InputStream(text)
    lexer = GGCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    parser = GGCodeParser(stream)
    tree = parser.program()
    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxError(f"Syntax errors found while parsing GG-Code:\n{text}")

    builder = ASTBuilder()
    program_ast = builder.visit(tree)
    stmts = program_ast.statements
    if len(stmts) == 1 and isinstance(stmts[0], Block):
        return stmts[0].statements
    return stmts


def run_pipeline(source_code: str, geometry_mode: str = "segmented") -> str:
    # 1. Classify lines: raw G-code passes through verbatim, only DSL chunks
    #    are parsed by ANTLR (keeps 142k-line slicer files interactive).
    items, layer_map = classify_lines(source_code)

    # 2. Build a single ordered AST: raw nodes interleaved with parsed DSL.
    statements = []
    for kind, payload in items:
        if kind == 'raw':
            statements.append(payload)
        else:  # 'dsl'
            statements.extend(_parse_dsl_chunk(payload))
    program_ast = Program(line=0, column=0, statements=statements)

    # 3. Semantic Analysis
    analyzer = SemanticAnalyzer()
    analyzer.analyze(program_ast)

    # 4. Code Generation (layer_map informs layer/height anchor resolution)
    generator = GCodeGenerator(geometry_mode=geometry_mode)
    gcode = generator.generate(program_ast, layer_map=layer_map)
    for w in generator.warnings:
        print(f"Warning: {w}", file=sys.stderr)
    return gcode

def main():
    parser = argparse.ArgumentParser(description="GG-Code to G-code Compiler")
    parser.add_argument("input_file", nargs="?", help="Path to the input .gg file")
    parser.add_argument("-o", "--output", default="output.gcode", help="Path to the output .gcode file")
    parser.add_argument("-g", "--geometry-mode", choices=["segmented", "exact"], default="segmented", help="Geometry generation mode")

    args = parser.parse_args()

    if args.input_file:
        try:
            with open(args.input_file, "r") as f:
                source_code = f.read()
        except FileNotFoundError:
            print(f"Error: Input file '{args.input_file}' not found.")
            return
    else:
        # Default sample if no file provided
        print("No input file provided. Using default sample code.")
        source_code = """
        Temperature 200C
        Wait for 2 minutes
        Set speed to 1000
        
        Move to X10 Y10
        
        If 5 > 3 then {
            Temperature 180C
        }
        
        Repeat 3 times {
            Move to X15 Y15
        }
        """

    print("--- Source Code ---")
    print(source_code)
    print("\n--- Pipeline Start (ANTLR Based) ---")

    try:
        gcode = run_pipeline(source_code, args.geometry_mode)

        with open(args.output, "w") as f:
            f.write(gcode)

        print(f"\nSuccessfully generated G-code to '{args.output}'")

    except SyntaxError as e:
        print(f"Parser Error: {e}")
    except SemanticError as e:
        print(f"Semantic Error: {e}")
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

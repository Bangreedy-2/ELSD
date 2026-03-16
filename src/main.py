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

def run_pipeline(source_code: str, geometry_mode: str = "segmented") -> str:
    # 1. Lexing
    input_stream = InputStream(source_code)
    lexer = GGCodeLexer(input_stream)
    stream = CommonTokenStream(lexer)
    stream.fill()

    # 2. Parsing
    parser = GGCodeParser(stream)
    tree = parser.program()

    if parser.getNumberOfSyntaxErrors() > 0:
        raise SyntaxError("Syntax errors found during parsing.")

    # 3. AST Construction
    builder = ASTBuilder()
    program_ast = builder.visit(tree)

    # 4. Semantic Analysis
    analyzer = SemanticAnalyzer()
    analyzer.analyze(program_ast)

    # 5. Code Generation
    generator = GCodeGenerator(geometry_mode=geometry_mode)
    return generator.generate(program_ast)

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

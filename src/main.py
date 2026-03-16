import sys
import os
from antlr4 import InputStream, CommonTokenStream

# Ensure we can run as script from inside src or root
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.antlr_gen.GGCodeLexer import GGCodeLexer
from src.antlr_gen.GGCodeParser import GGCodeParser
from src.parser.antlr_converter import ASTBuilder
from src.semantic.semantic_analyzer import SemanticAnalyzer
from src.semantic.semantic_errors import SemanticError
from src.codegen.gcode_generator import GCodeGenerator

def main():
    sample_code = """
    let speed = 100;
    let x = 10;
    let y = 20;

    move(x, y);

    if (x < 15) {
        move(0, 0);
    }

    let count = 2;
    repeat(count) {
        move(x + 5, y + 5);
        x = x + 10;
    }
    """

    print("--- Source Code ---")
    print(sample_code)
    print("\n--- Pipeline Start (ANTLR Based) ---")

    try:
        # 1. Lexing (ANTLR)
        print("[1] Lexing...")
        input_stream = InputStream(sample_code)
        lexer = GGCodeLexer(input_stream)
        stream = CommonTokenStream(lexer)
        stream.fill() # Force load

        # 2. Parsing (ANTLR) -> AST Conversion
        print("[2] Parsing...")
        parser = GGCodeParser(stream)
        tree = parser.program()

        if parser.getNumberOfSyntaxErrors() > 0:
            print("Syntax errors found.")
            return

        builder = ASTBuilder()
        program_ast = builder.visit(tree)
        print("AST generated successfully.")

        # 3. Semantic Analysis
        print("[3] Semantic Analysis...")
        # (This is just a validation pass, it doesn't execute code)
        analyzer = SemanticAnalyzer()
        analyzer.analyze(program_ast)
        print("Semantic check passed.")

        # 4. Code Generation
        print("[4] Generating G-code...")
        generator = GCodeGenerator()
        gcode = generator.generate(program_ast)

        print("\n--- Generated Output ---")
        print(gcode)

    except SemanticError as e:
        print(e)
    except Exception as e:
        import traceback
        traceback.print_exc()
        print(f"Error: {e}")

if __name__ == "__main__":
    main()


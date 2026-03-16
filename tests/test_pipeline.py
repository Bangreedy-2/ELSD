import pytest
import sys
import os

# Ensure src is in path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.main import run_pipeline

def test_basic_motion():
    source = "Move to X10 Y10"
    output = run_pipeline(source)
    assert "G1 X10 Y10" in output

def test_temperature_wait():
    source = """
    Temperature 200C
    Wait for 2 seconds
    """
    output = run_pipeline(source)
    assert "M104 S200" in output
    assert "G4 S2" in output

def test_repeat_loop():
    source = """
    Repeat 2 times {
        Move to X1 Y1
    }
    """
    output = run_pipeline(source)
    assert "; REPEAT 2 TIMES" in output
    # Body should appear twice
    assert output.count("G1 X1 Y1") == 2

def test_while_loop_compilation():
    source = """
    While 1 < 2 {
        Move to X0 Y0
    }
    """
    output = run_pipeline(source)
    assert "; WHILE LOOP" in output
    assert "G1 X0 Y0" in output

def test_geometry_square():
    source = "Add Square Center 0 0 Length 10"
    output = run_pipeline(source)
    # Check corners logic
    assert "G0 X-5.0 Y-5.0" in output
    assert "G1 X5.0 Y-5.0" in output

def test_geometry_circle_segmented():
    source = "Add Circle Center 0 0 Radius 10"
    output = run_pipeline(source, geometry_mode="segmented")
    assert "; Circle Segmented" in output
    # Check for G1 commands
    assert "G1 X" in output

def test_geometry_circle_exact():
    source = "Add Circle Center 0 0 Radius 10"
    output = run_pipeline(source, geometry_mode="exact")
    assert "G2 X10" in output or "G2 X10.0" in output
    assert "I-10" in output

def test_rectangle():
    source = "Add Rectangle Center 0 0 Width 20 Length 10"
    output = run_pipeline(source)
    # Half width 10, half length 5
    # X from -10 to 10, Y from -5 to 5
    assert "G0 X-10.0 Y-5.0" in output
    assert "G1 X10.0 Y-5.0" in output

def test_syntax_error():
    source = "Move 10" # Missing 'TO'
    with pytest.raises(SyntaxError):
        run_pipeline(source)

def test_semantic_error():
    source = "Move to unknown_place"
    from src.semantic.semantic_errors import SemanticError
    with pytest.raises(SemanticError):
        run_pipeline(source)



from src.evaluator import Evaluator

def test_basic_greens_and_yellows():
    ev = Evaluator()
    # They must implement duplicate-aware logic to make this pass
    assert ev.evaluate("trace", "track") == ['G','G','G','.','.']
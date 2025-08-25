from src.evaluator import Evaluator

def test_basic_greens_and_yellows():
    ev = Evaluator()
    # They must implement duplicate-aware logic to make this pass
    assert ev.evaluate("trace", "track") == ['G','G','G','G','.']

def test_yellows():
    ev = Evaluator()
    assert ev.evaluate("cider", "reidc") == ['Y', 'Y', 'Y', 'Y', 'Y']

def test_period():
    ev = Evaluator()
    assert ev.
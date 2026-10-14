import importlib.util
from pathlib import Path

path = Path(__file__).resolve().parents[1] / "codes" / "21_largest_word.py"
spec = importlib.util.spec_from_file_location("largest", path)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
largest_word = module.largest_word


def test_normal_sentence():
    assert largest_word("I love programming") == "programming"


def test_empty_sentence():
    assert largest_word("") == ""


def test_equal_length_words():
    assert largest_word("cat dog") == "cat"


def test_punctuation():
    assert largest_word("Hello, wonderful world!") == "wonderful"


def test_single_word():
    assert largest_word("Python") == "Python"
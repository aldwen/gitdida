from importlib.metadata import version
import sys


def test_version():
    print(sys.path)
    expected = "0.2.0"
    # assert distribution("src.gitdida").version == expect
    assert version("gitdida") == expected

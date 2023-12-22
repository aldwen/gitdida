from gitdida.__main__ import RunGitandDida
import pytest


def test_function():
    success, message = RunGitandDida()
    assert success == False
    assert message == "Need a git repository."

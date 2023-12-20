from src.gitdida.run import RunGitandDida


def test_function():
    success, message = RunGitandDida()
    assert success == 0
    assert message == "Need a git repotory"

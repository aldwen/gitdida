import pytest
from gitdida import dogit


def test_DoGit_run_with_right_parameters():
    repo_path = "~/coding/pystudy/ttt//.git"
    work_branch = "main"
    remote_name = "origin"
    git_succeed, message = dogit.run(repo_path, work_branch, remote_name)
    assert git_succeed == 1


#    assert "Succeed" in message

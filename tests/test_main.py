# import pytest
# import gitdida
# from click.testing import CliRunner


# @pytest.fixture
# def cli_runner():
#     return CliRunner()


# def test_main(cli_runner: CliRunner):
#     result = cli_runner.invoke(gitdida.__main__)
#     assert result.exit_code == 0
#     assert "Hello" in result.output


# from gitdida.functions import RunGitandDida


# def test_RunGitandDidan():
#     success, message = RunGitandDida()
#     assert success == False
#     assert message == "Need a git repository."

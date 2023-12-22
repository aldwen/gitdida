import pytest
from click.testing import CliRunner
import gitdida
from gitdida.cmdline import main, dojob, dodida


@pytest.fixture
def cli_runner():
    return CliRunner()


def test_version(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ["--version"])
    assert result.exit_code == 0
    assert gitdida.app_ver in result.output


def test_help(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ["--help"])
    assert result.exit_code == 0
    assert "A simple CLI application." in result.output


def test_run_default_workflow(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ["--run"])
    assert result.exit_code == 0
    assert "Executing the default workflow..." in result.output


def test_run_default_workflow_with_args(cli_runner: CliRunner):
    result = cli_runner.invoke(
        main,
        ["--run", "--repository", "my_repo", "--branch", "main", "--remote", "origin"],
    )
    assert result.exit_code == 0
    assert "dojob: repository=my_repo, branch=main, remote=origin" in result.output
    assert "dodida: executing additional steps..." in result.output


def test_run_dodida_only(cli_runner: CliRunner):
    result = cli_runner.invoke(main, ["--run", "--disable-dida"])
    assert result.exit_code == 0
    assert (
        "dojob: repository=default_repo, branch=default_branch, remote=default_remote"
        in result.output
    )
    assert "dodida: executing additional steps..." not in result.output


def test_dojob_with_args(cli_runner: CliRunner):
    result = cli_runner.invoke(
        main, ["--repository", "my_repo", "--branch", "main", "--remote", "origin"]
    )
    assert result.exit_code == 0
    assert "dojob: repository=my_repo, branch=main, remote=origin" in result.output
    assert "dodida: executing additional steps..." not in result.output


def test_dojob_with_args_and_dodida(cli_runner: CliRunner):
    result = cli_runner.invoke(
        main,
        [
            "--repository",
            "my_repo",
            "--branch",
            "main",
            "--remote",
            "origin",
            "--disable-dida",
        ],
    )
    assert result.exit_code == 0
    assert "dojob: repository=my_repo, branch=main, remote=origin" in result.output
    assert "dodida: executing additional steps..." not in result.output


# Add more tests based on your application's logic

if __name__ == "__main__":
    pytest.main()


# """Test cmdline"""
# import pytest
# from click.testing import CliRunner

# # from __future__ import annotations  # PEP 585
# from importlib.metadata import version
# from gitdida.cmdline import main


# _version = version("gitdida")


# @pytest.mark.parametrize(
#     ["invoke_args", "exit_code", "output_keyword"],
#     [
#         ([], 0, "help"),
#         (["--help"], 0, "help"),
#         (["--version"], 0, _version),
#         (["-V"], 0, _version),
#         (["--debug", "--verbose", "run"], 0, "run"),
#     ],
# )
# def test_main(
#     clicker: CliRunner,
#     invoke_args: list[str],
#     exit_code: int,
#     output_keyword: str,
# ):
#     """Test main cmdline"""
#     result = clicker.invoke(main, invoke_args)
#     assert result.exit_code == exit_code
#     assert output_keyword in result.output

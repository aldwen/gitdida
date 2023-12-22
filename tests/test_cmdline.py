import pytest
from click.testing import CliRunner
import gitdida
from gitdida.cmdline import cmdline, dojob, dodida


@pytest.fixture
def cli_runner():
    return CliRunner()


def test_version(cli_runner: CliRunner):
    result = cli_runner.invoke(cmdline, ["--version"])
    assert result.exit_code == 0
    assert gitdida.app_ver in result.output


def test_help(cli_runner: CliRunner):
    result = cli_runner.invoke(cmdline, ["--help"])
    assert result.exit_code == 0
    assert "Show this message and exit." in result.output


def test_run_default_workflow(cli_runner: CliRunner):
    result = cli_runner.invoke(cmdline)
    assert result.exit_code == 0
    assert "dodida: executing additional steps..." in result.output


def test_run_dojob_only(cli_runner: CliRunner):
    result = cli_runner.invoke(cmdline, ["-d"])
    assert result.exit_code == 0
    assert "dojob" in result.output
    assert "dodida: executing additional steps..." not in result.output


def test_dojob_with_args(cli_runner: CliRunner):
    result = cli_runner.invoke(
        cmdline,
        ["--repository", "rrr", "--branch", "bbb", "--remote", "ooo"],
    )
    assert result.exit_code == 0
    assert "dojob: repository=rrr, branch=bbb, remote=ooo" in result.output
    assert "dodida: executing additional steps..." in result.output


def test_dojob_with_args_and_no_dida(cli_runner: CliRunner):
    result = cli_runner.invoke(
        cmdline,
        [
            "--repository",
            "my_r",
            "--branch",
            "cmdline",
            "--remote",
            "gitee",
            "--disable-dida",
        ],
    )
    assert result.exit_code == 0
    assert "dojob: repository=my_r, branch=cmdline, remote=gitee" in result.output
    assert "dodida: executing additional steps..." not in result.output


# Add more tests based on your application's logic

if __name__ == "__cmdline__":
    pytest.cmdline()

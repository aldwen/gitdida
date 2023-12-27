"""
CMDline is main enterplace.
"""
import click
import gitdida
from gitdida import dogit, dodida
from gitdida.log import get_logger

logger = get_logger("GitDida.cmdline")


def print_version(ctx, param, value):
    if not value or ctx.resilient_parsing:
        return
    click.echo(f"{gitdida.app_name}, version {gitdida.app_ver}")
    ctx.exit()


@click.command()
@click.option(
    "-d", "--disable-dida", "nodida", is_flag=True, help="Disable add message to Dida."
)
@click.option(
    "--repository",
    type=str,
    help="Specify the repository, instead of from configuration.",
)
@click.option(
    "--branch",
    type=str,
    help="Specify the branch, instead of from configuration. ",
)
@click.option(
    "--remote",
    type=str,
    help="Specify the remote, instead of from configuration.",
)
@click.option(
    "--version",
    is_flag=True,
    callback=print_version,
    expose_value=False,
    is_eager=True,
    help="Show the version and exit.",
)
def cmdline(nodida, repository, branch, remote):
    git_succeed, message = dogit.run(repository, branch, remote)
    if not git_succeed:
        return False
    if not nodida:
        dodida.run()


if __name__ == "__main__":
    logger.info("Run ...")
    cmdline()

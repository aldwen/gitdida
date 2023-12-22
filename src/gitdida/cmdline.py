import click
import gitdida
from gitdida.config import settings
from gitdida.__main__ import dojob, dodida


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
    dojob(repository, branch, remote)
    if not nodida:
        dodida()


# def cmdrun( disable_dida, repository, branch, remote):
#     """A simple CLI application."""
#     if version:
#         click.echo(f"{prog_name}, version {app_version}")
#     elif help:
#         click.echo(main.get_help(ctx=None))
#     else:
#         if run or (not repository and not branch and not remote):
#             # Execute dojob with default values or provided values
#             dojob(repository, branch, remote)

#             # If disable-dida is not specified, continue with dodida
#             if not disable_dida:
#                 dodida()
#         else:
#             click.echo("No valid command specified. Use --help for usage information.")


if __name__ == "__main__":
    cmdline()


# """Command line"""
# import click
# from click import Context
# from importlib.metadata import version
# from gitdida.config import settings


# @click.group(invoke_without_command=True)
# @click.pass_context
# @click.option(
#     "-V", "--version", is_flag=True, help="Show version and exit."
# )  # If it's true, it will override `settings.VERBOSE`
# @click.option("-v", "--verbose", is_flag=True, help="Show more info.")
# @click.option(
#     "--debug", is_flag=True, help="Enable debug."
# )  # If it's true, it will override `settings.DEBUG`
# def main(ctx: Context, version: str, verbose: bool, debug: bool):
#     """Main commands"""
#     if version:
#         click.echo(version("gitdida"))
#     elif ctx.invoked_subcommand is None:
#         click.echo(ctx.get_help())
#     else:
#         if verbose:
#             settings.set("VERBOSE", True)
#         if debug:
#             settings.set("DEBUG", True)


# @main.command()
# def run():
#     """Run command"""
#     click.echo("run......")

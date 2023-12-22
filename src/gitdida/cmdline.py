import click
import gitdida
from gitdida.config import settings
from gitdida.__main__ import dojob, dodida


@click.command()
@click.option("--help", is_flag=True, help="Display help message.")
@click.option("--run", is_flag=True, help="Execute the default workflow.")
@click.option("--version", is_flag=True, help="Display version number.")
@click.option("--disable-dida", is_flag=True, help="Disable dida feature.")
@click.option("--repository", type=str, help="Specify the repository.")
@click.option("--branch", type=str, help="Specify the branch.")
@click.option("--remote", type=str, help="Specify the remote.")
@click.version_option(version=gitdida.app_ver, prog_name=gitdida.app_name)
def main(help, run, version, disable_dida, repository, branch, remote):
    """A simple CLI application."""
    if version:
        click.echo(f"{prog_name}, version {app_version}")
    elif help:
        click.echo(main.get_help(ctx=None))
    else:
        if run or (not repository and not branch and not remote):
            # Execute dojob with default values or provided values
            dojob(repository, branch, remote)

            # If disable-dida is not specified, continue with dodida
            if not disable_dida:
                dodida()
        else:
            click.echo("No valid command specified. Use --help for usage information.")


if __name__ == "__main__":
    main()


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

"""
Configuration center.
Use https://www.dynaconf.com/
""" ""
import sys
from pathlib import Path

from dynaconf import Dynaconf


_base_dir = Path(__file__).parent.parent

_settings_files = [
    Path(__file__).parent / "settings.toml",
    Path(__file__).parent / ".secrets.toml",
]

# User configuration. It will be created automatically by the pip installer .
_external_files = [Path(sys.prefix, "etc", "gitdida", "settings.toml")]


settings = Dynaconf(
    envvar_prefix="GITDIDA",
    settings_files=_settings_files,  # load user configuration.
    # environments=True,  # Enable multi-level configuration，eg: default, development, production
    # load_dotenv=True,  # Enable load .env
    # env_switcher="GITDIDA_ENV",
    # includes=_external_files,  # Customs settings.
    base_dir=_base_dir,  # `settings.BASE_DIR`
)

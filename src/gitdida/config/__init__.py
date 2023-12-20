"""
Configuration center.
Use https://www.dynaconf.com/
""" ""
import os
import sys
from pathlib import Path

from dynaconf import Dynaconf


_base_dir = Path(__file__).parent.parent

_settings_files = [
    # All config file will merge.
    Path(__file__).parent
    / "settings.toml",  # Load default config.
]

# User configuration. It will be created automatically by the pip installer .
_external_files = [Path(sys.prefix, "etc", "gitdida", "settings.toml")]


settings = Dynaconf(
    # Set env `gitdida_FOO='bar'`，use `settings.FOO` .
    envvar_prefix="gitdida",
    settings_files=_settings_files,  # load user configuration.
    # environments=True,  # Enable multi-level configuration，eg: default, development, production
    load_dotenv=True,  # Enable load .env
    # env_switcher='gitdida_ENV',
    lowercase_read=False,  # If true, can't use `settings.foo`, but can only use `settings.FOO`
    includes=_external_files,  # Customs settings.
    base_dir=_base_dir,  # `settings.BASE_DIR`
)

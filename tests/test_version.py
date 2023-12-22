import pytest
from importlib.metadata import version
import gitdida


def test_dont_forgot_increase_version():
    lastVersion = "0.2.0"
    print(f"LastVersion is:{lastVersion}")
    assert version("gitdida") > lastVersion, f" Current Version still is {lastVersion}"


def test_name_in_package():
    assert gitdida.app_name == "gitdida"


def test_version_in_package():
    assert gitdida.app_ver == version(gitdida.app_name)

import sys
import subprocess


def test_if_installed():
    assert not(subprocess.call(["pip", "show", "hunana"]))


def test_if_can_import():
    try:
        from hunana import Hunana
    except:
        assert False

    assert True


def test_cli():
    process = subprocess.run(['hunana', '-h'], shell=True)

    assert process.returncode == 0
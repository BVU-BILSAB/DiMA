import subprocess


def test_if_installed():
    assert not(subprocess.run(["pip", "show", "hunana"]).stdout)


def test_if_can_import():
    try:
        from hunana import Hunana
    except:
        assert False

    assert True


def test_cli():
    process = subprocess.run(['hunana', '-h'])

    assert process.returncode == 0
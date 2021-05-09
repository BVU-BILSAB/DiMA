import subprocess


def test_if_installed():
    assert not(subprocess.run(["pip", "show", "dima-cli"]).stdout)


def test_if_can_import():
    try:
        from dima import Dima
    except:
        assert False

    assert True


def test_cli():
    process = subprocess.run(['dima-cli', '-h'])

    assert process.returncode == 0
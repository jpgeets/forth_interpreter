from forth_interpreter.cli import main


def test_cli_success(capsys):
    exit_code = main(["3", "4", "+"])

    captured = capsys.readouterr()
    assert exit_code == 0
    assert captured.out.strip() == "[7]"


def test_cli_error(capsys):
    exit_code = main(["3", "unknown"])

    captured = capsys.readouterr()
    assert exit_code == 1
    assert "Error:" in captured.out

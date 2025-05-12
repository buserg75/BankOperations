import os
import tempfile

from src.decorators import add, log


def test_add_with_decorator(capsys):
    assert add(4, 2) == 6
    captured = capsys.readouterr()
    assert captured.out == ''


def test_log_success(capsys):
    @log()
    def test_add(a, b):
        return a + b

    test_add(1, 2)
    captured = capsys.readouterr()
    assert 'test_add ok' in captured.out


def test_log_to_file():
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        filename = tmp.name

    @log(filename=filename)
    def test_add(a, b):
        return a + b

    test_add(4, 2)
    with open(filename) as f:
        content = f.read()
    os.unlink(filename)
    assert "test_add ok" in content


def test_log_error(capsys):
    @log()
    def test_divide(a, b):
        raise ValueError('test error')

    test_divide(1, 0)
    captured = capsys.readouterr()
    assert 'test_divide error: ValueError' in captured.out
    assert 'Inputs: (1, 0), {}' in captured.out

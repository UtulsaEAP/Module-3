'''
Test cases for the right_arrow module.
'''
import smallest_num as smallest_num
def test_one(monkeypatch, capsys):
    inputs = iter(["7", "15", "3"])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "3" in all_outputs, "Make sure that only the smallest number is printed"

def test_two(monkeypatch, capsys):
    inputs = iter(["29", "6", '17'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "6" in all_outputs, "Make sure that only the smallest number is printed"

def test_three(monkeypatch, capsys):
    inputs = iter(["3", "2", '1'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "1" in all_outputs, "Make sure that only the smallest number is printed"

def test_four(monkeypatch, capsys):
    inputs = iter(["7", "7", '7'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "7" in all_outputs, "Make sure that only the smallest number is printed"

def test_five(monkeypatch, capsys):
    inputs = iter(["6", "10", '10'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "6" in all_outputs, "Make sure that only the smallest number is printed"

def test_six(monkeypatch, capsys):
    inputs = iter(["5", "3", '5'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "3" in all_outputs, "Make sure that only the smallest number is printed"

def test_seven(monkeypatch, capsys):
    inputs = iter(["12", "12", '15'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "12" in all_outputs, "Make sure that only the smallest number is printed"

def test_eight(monkeypatch, capsys):
    inputs = iter(["5", "7", '5'])
    monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
    smallest_num.smallest_number()
    captured = capsys.readouterr()
    all_outputs = captured.out
    assert "5" in all_outputs, "Make sure that only the smallest number is printed"

'''
Test cases for the leap_year module.
'''
import leap_year as leap_year
ERROR_MSG = "Not a leap year"
VALID_LEAP_YEAR = "Leap year"

class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["1954"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        leap_year.leap_year()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')
        assert "1954 - not a leap year" in all_outputs , ERROR_MSG

    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["2016"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        leap_year.leap_year()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "2016 - leap year" in all_outputs, VALID_LEAP_YEAR

    def test_three(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["1600"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        leap_year.leap_year()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "1600 - leap year" in all_outputs, VALID_LEAP_YEAR

    def test_four(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["1900"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        leap_year.leap_year()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "1900 - not a leap year"in all_outputs , ERROR_MSG

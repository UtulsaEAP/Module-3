'''
Test cases for the exact_change module.
'''
import exact_change as exact_change
ERROR_MSG = "Ensure proper grammar in the output, IE 1 dollar vs 2 dollars, 1 penny vs 2 pennies, etc."
DOMAIN_ERROR = "0 is not a valid amount of money"
class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["45"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        exact_change.exact_change()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')

        assert all(x in all_outputs for x in ['1 Quarter','2 Dimes']) , ERROR_MSG

    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["0"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        exact_change.exact_change()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "No change" in all_outputs , DOMAIN_ERROR

    def test_three(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["156"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        exact_change.exact_change()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert all(x in all_outputs for x in ["1 Dollar","2 Quarters", "1 Nickel", "1 Penny"]) , ERROR_MSG

    def test_four(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["300"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        exact_change.exact_change()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "3 Dollars" in all_outputs , ERROR_MSG

    def test_five(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["141"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        exact_change.exact_change()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert all(x in all_outputs for x in ['1 Dollar','1 Quarter', '1 Dime','1 Nickel', '1 Penny']), ERROR_MSG

    
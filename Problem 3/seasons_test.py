'''
Test cases for the seasons module.
'''
import seasons as seasons
SPRING_ERROR = "Spring is between March 20 and June 20 in the Northern Hemisphere"
FALL_ERROR = "Autumn is between September 22 and December 20 in the Northern Hemisphere"
WINTER_ERROR = "Winter is between December 21 and March 19 in the Northern Hemisphere"
SUMMER_ERROR = "Summer is between June 21 and September 21 in the Northern Hemisphere"
DOMAIN_ERROR = "The month must be a valid month and the day must be a valid day of the month"
class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["April","11"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Spring" in all_outputs , SPRING_ERROR

    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["March","3"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Winter" in all_outputs , WINTER_ERROR

    def test_three(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["Word","21"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Invalid" in all_outputs , DOMAIN_ERROR

    def test_four(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["February","39"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Invalid" in all_outputs , DOMAIN_ERROR

    def test_five(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["June","21"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Summer" in all_outputs , SUMMER_ERROR

    def test_six(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["November","7"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Autumn" in all_outputs , FALL_ERROR

    def test_seven(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["September","31"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Invalid" in all_outputs , DOMAIN_ERROR
    
    def test_eight(self,monkeypatch,capsys):
        inputs = iter(["December","-1"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Invalid" in all_outputs , DOMAIN_ERROR

    def test_nine(self,monkeypatch,capsys):
        #input february 0
        inputs = iter(["February","0"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Invalid" in all_outputs , DOMAIN_ERROR
    
    def test_ten(self,monkeypatch,capsys):
        #input october 31
        inputs = iter(["October","31"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))
        seasons.seasons()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Autumn" in all_outputs , FALL_ERROR
        
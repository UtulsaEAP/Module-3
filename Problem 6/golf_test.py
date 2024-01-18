'''
Test cases for the golf module.
'''
import golf as golf
EAGLE_ERROR = "Eagle is two less than par"
BIRDIE_ERROR = "Birdie is one less than par"
BOGEY_ERROR = "Bogey is one more than par"
PAR_ERROR = "Par is the same as par"


class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["4","3"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        golf.golf()
        captured = capsys.readouterr()
        all_outputs = captured.out.split('\n')
        assert "Birdie" in all_outputs , BIRDIE_ERROR
        
    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["5","3"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        golf.golf()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Eagle" in all_outputs, EAGLE_ERROR

    def test_three(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["5","5"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        golf.golf()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Par" in all_outputs, PAR_ERROR

    def test_four(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["5","6"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        golf.golf()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Bogey" in all_outputs , BOGEY_ERROR
    
    def test_five(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["1","2"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        golf.golf()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "Error" in all_outputs , "Par must be between 3 and 5 inclusive"

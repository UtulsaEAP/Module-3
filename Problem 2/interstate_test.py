'''
Test cases for the interstate module.
'''
import interstate as interstate

EVEN_ERROR = "Even numbered highways are east/west"
ODD_ERROR = "Odd numbered highways are north/south"
AUX_ERROR = "Auxiliary highways service their primary highway indicated by the rightmost two digits"
DOMAIN_ERROR = "Highway numbers must be between 1 and 999 inclusive and service valid highways"
class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["90"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        interstate.interstate()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "I-90 is primary, going east/west" in all_outputs , EVEN_ERROR
       
    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["290"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        interstate.interstate()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "I-290 is auxiliary, serving I-90, going east/west." in all_outputs , EVEN_ERROR + " " + AUX_ERROR

    def test_three(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["0"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        interstate.interstate()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "0 is not a valid interstate highway number." in all_outputs , DOMAIN_ERROR

    def test_four(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["200"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        interstate.interstate()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "200 is not a valid interstate highway number." in all_outputs , DOMAIN_ERROR

    def test_five(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["5"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        interstate.interstate()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "I-5 is primary, going north/south." in all_outputs , ODD_ERROR

    def test_six(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["405"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        interstate.interstate()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "I-405 is auxiliary, serving I-5, going north/south" in all_outputs , ODD_ERROR + " " + AUX_ERROR

    def test_seven(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["1000"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        interstate.interstate()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "1000 is not a valid interstate highway number." in all_outputs , DOMAIN_ERROR

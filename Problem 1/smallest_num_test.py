'''
Test cases for the right_arrow module.
'''
import smallest_num as smallest_num

class TestClass:
    def test_one(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["7", "15","3"])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "3" in all_outputs , "Make sure that only the smallest number is printed"
       
    def test_two(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["29", "6",'17'])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "6" in all_outputs , "Make sure that only the smallest number is printed"

    def test_three(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["3", "2",'1'])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "1" in all_outputs , "Make sure that only the smallest number is printed"

    def test_four(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["7", "7",'7'])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "7" in all_outputs , "Make sure that only the smallest number is printed"

    def test_five(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["6", "10",'10'])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "6" in all_outputs , "Make sure that only the smallest number is printed"

    def test_six(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["5", "3",'5'])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "3" in all_outputs , "Make sure that only the smallest number is printed"

    def test_seven(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["12", "12",'15'])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "12" in all_outputs , "Make sure that only the smallest number is printed"

    def test_eight(self,monkeypatch,capsys):

        # monkeypatch the "input" function, so that it returns "Mark".
        # This simulates the user entering "Mark" in the terminal:
        inputs = iter(["5", "7",'5'])
        monkeypatch.setattr('builtins.input', lambda: next(inputs, '\n'))

        # go about using input() like you normally would:
        smallest_num.smallest_number()
        captured = capsys.readouterr()
        all_outputs = captured.out
        assert "5" in all_outputs , "Make sure that only the smallest number is printed"
    
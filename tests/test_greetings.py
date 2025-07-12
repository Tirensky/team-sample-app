from app.greetings import say_hello

def test_say_hello(capsys):
    say_hello("team")
    captured = capsys.readouterr()
    assert "Hello, team!" in captured.out

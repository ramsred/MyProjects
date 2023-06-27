from hello import hello_more


def test_hello():
    assert "hi" == hello_more()


def test_hello2():
    assert "bye" == hello_more()

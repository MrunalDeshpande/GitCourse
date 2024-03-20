import pytest


@pytest.mark.smoke
@pytest.mark.skip
def test_firstProgram():
    msg = "Hello"
    assert msg == "Hi", "Test failed because string do not match"


def test_secondCreditCard():
    a = 2
    b = 4
    assert a + 4 == 6, "Addition do not match"

@pytest.fixture()
def setup():
    print("I will be executed first")

def test_fixtureDemo(setup):
    print("I will execute steps in fixtureDemo method")
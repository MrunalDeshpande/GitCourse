import pytest


@pytest.fixture(scope='class')
def setup():
    print("I will executing first")
    yield
    print("I will executing last")


@pytest.fixture()
def dataLoad():
    print("User profile is being create")
    return ["Mrunal", "Deshpande", "rahulshettyacademy.com"]


@pytest.fixture(params=[("chrome","Mrunal","Deshpande"), ("Firefox","Manaswi"), ("IE","Madhav")])
def crossBrowser(request):
    return request.param

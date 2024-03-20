# Any Pytest file should start with test_ or end with _test
# pytest method names should start with test
# Any code should be wrapped in method only
#Method names should have sense
#- k - method names execution, - s -> logs in output , -v -> Stands fro more info metadata
#you can run specific file with py.test<filename>
#you can mark (tag) tests @pytest.mark.smoke and then run with -m
# you can skip tests with @pytest.mark.skip
#fixtures are used for setup and teardown methods for test cases, conftest file to generalize fixture and make it available to all test cases
#fixture are make it available to all test cases (fixture name into parameters of method)
#datadriven and parameterization can be done with return statement in tuple format
#when you define fixtures scope to class only, it will run once before class is intiated at the end

import pytest
@pytest.mark.smoke
def test_firstProgram():
    print("Hello")

@pytest.mark.xfail
def test_SecondGreetCreditCard():
    print("Good Morning")

def test_crossBrowser(crossBrowser):
    print(crossBrowser[1] )
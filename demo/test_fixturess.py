import pytest


@pytest.fixture(scope='class')
def test_abc():
    print("this is before method")
    yield
    print("this is after method")
def test_m1():
    print("this is m1")
def test_m2():
    print("this is m2")
#@pytest.mark.usefixtures('test_abc')
def test_m3():
    print("this is m3")

@pytest.mark.usefixtures("test_abc")
class Test():
    def test_s1(self):
        print("this is test s1")



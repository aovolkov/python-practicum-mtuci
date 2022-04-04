import pytest

x = 5
y = 6

set1 = set("1310")
set2 = set("8035")

class Foo:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val

f1 = Foo(1)
f2 = Foo(2)

def test_file1_method1():
    assert x + 1 == y, "test failed"
    assert x == y, "test failed"


def test_file1_method2():
    assert x + 1 == y, "test failed"

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
         1 / 0

def test_set_comparison():
    assert set1 == set2

def test_compare():
    assert f1 == f2

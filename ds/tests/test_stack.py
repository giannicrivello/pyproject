from ds.stack import Stack
import pytest

@pytest.fixture
def stack():
    return Stack()

def test_constuctor():
    s = Stack()
    assert isinstance(s, Stack)
    assert len(s) == 0

def test_push(stack):
    stack.push(3)
    assert len(stack) == 1
    stack.push(5)
    assert len(stack) == 2

def test_pop(stack):
    stack.push('Hello')
    stack.push('World')
    assert stack.pop() == "World"
    assert stack.pop() == "Hello"
    assert stack.pop() is None
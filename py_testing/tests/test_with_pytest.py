from py_testing.code import Test

def test_uppercase():
    t = Test()
    assert t.uppercase("hello") == "HELLO"

def test_reverse_list():
    t = Test()
    assert t.reverse_list([1,2,3,4]) == [4,3,2,1]

def test_request_people():
    t = Test()
    assert t[0] == t.people[0]

def test_dispatcher():
    t = Test()
    assert t.dispatcher("add", 2, 2) == 4
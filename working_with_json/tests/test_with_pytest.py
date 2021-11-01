import json
import requests
from code.Working_with_json import ToDo


def test_api_call():
    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    todos = json.loads(response.text)
    assert todos == response.json()


def test_indexing():
    t = ToDo()
    assert t[0] == t.todos[0]

def test_completed_tasks():
    t = ToDo()
    todos_by_user = {}
    for todo in t._todos:
        if todo['completed'] == True:
            todos_by_user[todo['userId']] += 1
        else:
            todos_by_user[todo['userId']] = 1
    



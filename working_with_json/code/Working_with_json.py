import json
import requests

class ToDo:

    _response = requests.get("https://jsonplaceholder.typicode.com/todos")
    _todos = json.loads(_response.text)

    def __getitem__(self, position):
        return self._todos[position]

    def completed_tasks(self):
        todos_by_user = {}

        for todo in self._todos:
            if todo['completed']:
                try:
                    todos_by_user[todo['userId']] =+ 1
                except KeyError:
                    todos_by_user[todo['userId']] = 1
        top_users = sorted(todos_by_user.items(),
        key=lambda x: x[1], reverse=True)

        max_completed = top_users[0][1]

        users = []
        for user, num_complete in top_users:
            if num_complete < max_completed:
                break
            users.append(str(user))
        max_users = " and ".join(users)
        s = "s" if  len(users) > 1 else ""
        print(f"user{s} {max_users} completed {max_completed} TODOS")


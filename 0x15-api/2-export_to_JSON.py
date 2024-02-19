#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests
from sys import argv

if __name__ == "__main__":
    num = argv[1]
    r = requests.get(
        f'https://jsonplaceholder.typicode.com//users/{num}/todos'
        )
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{num}"
                        ).json()

    rjson = r.json()
    todos = []
    for todo in rjson:
        data = {"task": todo['title'],
                "completed": todo['completed'], "username": user['username']}
        todos.append(data)

    dictdata = {str(user['id']): todos}
    with open(f"{user['id']}.json", 'w') as fp:
        json.dump(dictdata, fp, indent=2)

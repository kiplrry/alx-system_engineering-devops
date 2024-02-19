#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import json
import requests


if __name__ == "__main__":
    todos = requests.get(
        f'https://jsonplaceholder.typicode.com/todos'
        ).json()
    users = requests.get(
        f"https://jsonplaceholder.typicode.com/users"
        ).json()

    usersdata = {}
    usersdict = {}
    for user in users:
        usersdict[user['id']] = user
        usersdata[user['id']] = []

    for todo in todos:
        userid = todo['userId']
        data = {"task": todo['title'],
                "completed": todo['completed'],
                "username": usersdict[userid]['username']}
        usersdata[userid].append(data)

    with open("todo_all_employees.json", 'w') as fp:
        json.dump(usersdata, fp, indent=2)

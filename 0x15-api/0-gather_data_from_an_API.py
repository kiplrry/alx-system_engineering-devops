#!/usr/bin/python3

import requests
from sys import argv

num = argv[1]
r = requests.get(f'https://jsonplaceholder.typicode.com/todos?userId={num}')
name = requests.get(f"""https://jsonplaceholder.typicode.com/users/{num}""")\
    .json()['name']


rjson = r.json()
alltodos = len(rjson)
donetodos = 0
todos = ""
for todo in rjson:
    if todo["completed"] is True:
        donetodos += 1
    todos += f"\n\t {todo['title']}"

statement = f"Employee {name} is done with tasks({donetodos}/{alltodos}):\
    {todos}"
print(statement)

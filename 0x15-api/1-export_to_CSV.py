#!/usr/bin/python3
"""script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""
import requests
from sys import argv

if __name__ == "__main__":
    num = argv[1]
    r = requests.get(
        f'https://jsonplaceholder.typicode.com//users/{num}/todos'
        )
    name = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{num}"
                        ).json()['name']

    rjson = r.json()

    with open(f"{num}.csv", "w", encoding="utf-8") as fp:
        for todo in rjson:
            string = (f"\"{todo['userId']}\",\"{name}\","
                      f"\"{todo['completed']}\",\"{todo['title']}\"\n")
            fp.write(string)

#!/usr/bin/python3
"""Export to all JSON"""
import json
import requests as req

base_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    res = req.get(f"{base_url}/users")
    users = res.json()
    d = dict()
    for user in users:
        id = user['id']
        username = user['username']
        res = req.get(f"{base_url}/users/{id}/todos/")
        tasks = res.json()
        d[f"{id}"] = list()
        for todo in tasks:
            d[f"{id}"].append({"username": username, "task": todo['title'],
                               "completed": todo['completed']})
    with open("todo_all_employees.json", 'w') as f:
        json.dump(d, f)

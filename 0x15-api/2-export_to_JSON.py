#!/usr/bin/python3
"""Export to CSV"""
import json
import requests as req
import sys

base_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    id = sys.argv[1]
    res = req.get(f"{base_url}/users/{id}")
    res = res.json()
    username = res['username']
    res = req.get(f"{base_url}/users/{id}/todos/")
    res = res.json()
    ntodos = len(res)
    ndone = 0
    tasks = list()
    d = {f"{id}": tasks}
    for todo in res:
        tasks.append({"task": todo['title'], "completed": todo['completed'],
                      "username": username})
    with open(f"{id}.json", 'w') as f:
        json.dump(d, f)

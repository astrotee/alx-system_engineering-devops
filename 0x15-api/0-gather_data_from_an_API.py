#!/usr/bin/python3
"""Gather data from an API"""
import requests as req
import sys

base_url = "https://jsonplaceholder.typicode.com"

if __name__ == "__main__":
    id = sys.argv[1]
    res = req.get(f"{base_url}/users/{id}")
    res = res.json()
    name = res['name']
    res = req.get(f"{base_url}/users/{id}/todos/")
    res = res.json()
    ntodos = len(res)
    ndone = 0
    done_tasks = []
    for todo in res:
        if todo['completed']:
            ndone += 1
            done_tasks.append(todo['title'])
    print(f"Employee {name} is done with tasks({ndone}/{ntodos}):")
    for title in done_tasks:
        print(f"\t {title}")

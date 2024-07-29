#!/usr/bin/python3
"""Export to CSV"""
import sys
import requests as req

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
    with open(f"{id}.csv", 'w') as f:
        for todo in res:
            f.write(f'"{id}","{username}","{todo['completed']}","{todo['title']}"\n')

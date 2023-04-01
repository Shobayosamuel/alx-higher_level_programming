#!/usr/bin/python3
"""
    Python script that takes your GitHub credentials
    (username and password) and uses the GitHub API
    to display your id
"""
import sys
import requests


if __name__ == "__main__":
    password = sys.argv[2]
    username = sys.argv[1]
    response = requests.get("https://api.github.com/user",
                            auth=(username, password))
    if response.status_code == 200:
        data = response.json()
        print(data.get('id'))
    else:
        print("None")

#!/usr/bin/python3
"""
    A python script that receives two arguments
    from the command line and use it to fetch requests
    to the github API and return ten mosts recent commits made
"""
import sys
import requests


if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    response = requests.get(url)
    data = response.json()
    try:
        for i in range(10):
            sha = data[i]["sha"]
            name = data[i]["commit"]["author"]["name"]
            print(f"{sha}: {name}")
    except IndexError:
        pass

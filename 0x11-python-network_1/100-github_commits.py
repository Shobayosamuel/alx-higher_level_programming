#!/usr/bin/python3

import sys
import requests

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    response = requests.get(f"https://api.github.com/repos/\
                            {owner_name}/{repo_name}/commits")
    data = response.json()
    try:
        for i in range(10):
            print("{}: {}".format(data[i]["sha"],
                  data[i]["commit"]["author"]["name"]))
    except IndexError:
        pass

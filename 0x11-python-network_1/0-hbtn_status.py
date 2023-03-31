#!/usr/bin/python3
"""Python script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == "__main__":
    from urllib import request
    req = request.Request('https://alx-intranet.hbtn.io/status')
    with request.urlopen(req) as response:
        page = response.read()
        print("Body response:")
        print(f"\t- type: {type(page)}")
        print(f"\t- content: {page}")
        print(f"\t- utf8 content: {page.decode('utf-8')}")

#!/usr/bin/python3
"""Write a Python script that takes in a URL, sends a request to the URL"""

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        content = response.headers.get('X-Request-Id')
        print(content)

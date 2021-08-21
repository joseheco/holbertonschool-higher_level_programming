#!/usr/bin/python3
""" Python script that takes in a URL, sends a request to the URL"""

if __name__ == "__main__":
    import sys
    import requests

    url = sys.argv[1]
    response = requests.get(url)
    if (response.status_code >= 400):
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)

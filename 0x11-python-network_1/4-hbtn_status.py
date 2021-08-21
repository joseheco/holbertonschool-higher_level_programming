#!/usr/bin/python3
"""Python script that fetches https://intranet.hbtn.io/status"""

if __name__ == "__main__":
    import requests

    reque = requests.get('https://intranet.hbtn.io/status')
    print("Body response:\n\t- type: {}\n\t- content: {}"
          .format(type(reque.text), reque.text))

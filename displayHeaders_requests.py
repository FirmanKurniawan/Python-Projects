import requests


def main():
    uri = requests.get("https://archiko.my.id")
    return uri.headers

if __name__=="__main__":
   main()

import requests
import attrs


@attrs.define
class ScanningDirectory:
    url : str

    def scanning(self, dir : str) -> str:
        join_url = self.url + "/"+ dir
        req = requests.get(join_url)
        if req.status_code == 200:
            print(f"{join_url} : {req.status_code}")
        else:
            print(f"{join_url} : {req.status_code}")

if __name__ == '__main__':
    url = "url"
    with open("c:/Users/adriy/Documents/list.txt") as f:
       for line in f:
           try:
               d = ScanningDirectory(url)
               d.scanning(line)
           except:
               continue



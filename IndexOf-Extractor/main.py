# this tool uncomplete
# main.py <url index of>
# e.g https://google.com/vendor (index of page)

# origin repo https://github.com/xhiko1/extract-if

import requests
import re, os, sys

class extfi:

    def __init__(self,path):
        self._path = path

#        if not self._path.endswith('/'):
#            self._path = self._path + '/'

        self._path=self._path+'/' if not self._path.endswith('/') else self._path
        self._host = re.findall(r'^(http|https)\:\/\/(.*?)/',self._path)[0]
        self.__reqs = requests.get(self._path).text
        self.__createFolder(self._host[1])


    @staticmethod
    def Download(url,h,f):
        uf = requests.get(f"{url}",allow_redirects=True)
        print (f'{uf.url} (\033[92m{uf.status_code}\033[97m)')

        with open(f'{h}/{f}','wb') as f:
            f.write(uf.content)
        return 0

    @staticmethod
    def __createFolder(dirname):
        if os.path.exists(dirname):
            pass
        else:
            return os.makedirs(dirname)

    #cdof: dir or file sorter
    @staticmethod
    def cdof(route):
        if route.endswith('/'):
            return {'type':'dir'}
        return {'type':'file'}

        
    def getHref(self,reqs):
        self._req = reqs
        self.__href = re.findall(r'href="(.*?)"',self._req)

        def clean(__):
            ___ = []
            for _ in __:
                if _.startswith('?C'):
                    continue
                if '/' in _:
                    if len(_) == int(1):
                        continue
                    ___.append(_)
                else:
                    ___.append(_)
            return ___

        return clean(self.__href)


    def extract(self):
        self.__status = True
        for name in self.getHref(self.__reqs):
            if self.cdof(name)["type"] == "file":
                self.Download(self._path+name,self._host[1],name)

        return 0

class main():
    ex = extfi(sys.argv[1])

    def __init__(self):
        self.ex.extract() 
        
        
if __name__=="__main__":
    run = main()

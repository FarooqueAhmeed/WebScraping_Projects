import urllib3
from bs4 import BeautifulSoup


def getName():
    http = urllib3.PoolManager()
    req = http.request('GET', 'https://www.worldometers.info/coronavirus/')
    print(req.status)
    if req.status == 200:
        soup = BeautifulSoup(req.data)
        mainC = soup.findAll('div', {'id': 'maincounter-wrap'})
        for counter in mainC:
            try:
                HashOne = counter.findAll('h1')
                for HashOneR in HashOne:
                    StringHash = HashOneR.text

                spanR = counter.findAll('span')
                for spaner in spanR:
                    spanS = spaner.text
                    try:

                        print(StringHash)
                        print(spanS)
                    except AttributeError:
                        continue
            except AttributeError:
                continue


    country_name = input("Enter Name :")
    http = urllib3.PoolManager()
    req = http.request('GET', 'https://www.worldometers.info/coronavirus/country/' + country_name)
    print(req.status)
    if req.status == 200:
        soup = BeautifulSoup(req.data)
        mainC = soup.findAll('div', {'id': 'maincounter-wrap'})
        for counter in mainC:
            try:
                HashOne = counter.findAll('h1')
                for HashOneR in HashOne:
                    StringHash = HashOneR.text

                spanR = counter.findAll('span')
                for spaner in spanR:
                    spanS = spaner.text
                    try:

                        print(StringHash)
                        print(spanS)
                    except AttributeError:
                        continue
            except AttributeError:
                continue


if __name__ == "__main__":
    getName()

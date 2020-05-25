import urllib3
from bs4 import BeautifulSoup


def getName():
    country_name= input("Enter Name :")
    http = urllib3.PoolManager()
    req = http.request('GET', 'https://www.worldometers.info/coronavirus/country/'+country_name)
    print(req.status)
    if req.status == 200:
       soup = BeautifulSoup(req.data)
       mainC = soup.findAll('div', {'id': 'maincounter-wrap'})
       for counter in mainC:
           try:
              HashOne = counter.findAll('h1')
              for HashOneR in HashOne:
                   StringHash = HashOneR.text
                   try:
                        print(StringHash)


if __name__ == "__main__":
     getName()


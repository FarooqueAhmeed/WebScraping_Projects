import urllib3
from bs4 import BeautifulSoup

def olx():
     user_agent = {'user-agent': 'Mozilla/5.0 (Windows NT 6.3; rv:36.0) ..'}
     http = urllib3.PoolManager(10, headers=user_agent)
     req = http.request('GET', 'https://www.olx.com.pk/larkana_g4060697/mobile-phones_c1453')
     print(req.status)
     if req.status == 200:
         soup = BeautifulSoup(req.data)
         classIK = soup.findAll('div', {'class': 'IKo3_'})
         for detail in classIK:
                 spanR = detail.findAll('span')
                 for spaner in spanR:
                     spanS = spaner.text
                     print(spanS)






if __name__ == "__main__":
    olx()
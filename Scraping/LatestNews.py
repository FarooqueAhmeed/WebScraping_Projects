import urllib3
from bs4 import BeautifulSoup


def getLatestNews():
    http = urllib3.PoolManager()
    req = http.request('GET', 'https://www.dawn.com/latest-news')
    print(req.status)
    if req.status == 200:
        soup = BeautifulSoup(req.data)
        # print(soup.prettify())
        news_article = soup.findAll('article', {'class': 'box'})

        for news in news_article:
            try:
                news_parts = news.findAll('h2')
                news_time_excerpt_parts = news.findAll('div', {'class': 'story__excerpt'})
                for part in news_parts:
                    news_head = part.text
                    news_id = part['data-id']
                    news_link = part.find('a', {'class':'story__link'})['href']
                    try:
                        if len(news_time_excerpt_parts) > 0:
                            news_excerpt = news_time_excerpt_parts[0].text
                        else:
                            print()
                        print(news_head)
                        print(news_excerpt)

                        with open("news.txt", "a") as text_file:
                            text_file.write(news_id+'\n'+news_link+'\n'+news_head + '\n\n' + news_excerpt + "\n\n\n")
                    except AttributeError:
                        continue

                # print news.find('h2').text
            except AttributeError:
                continue
    else:
        print("Response was other than 200.")


if __name__ == "__main__":
    getLatestNews()
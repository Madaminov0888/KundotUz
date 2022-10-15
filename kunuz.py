import requests
from bs4 import BeautifulSoup
import lxml
import selenium
from selenium import webdriver


MAIN_URL = 'https://kun.uz'



def parse_kun_uz(MAX_NUMBER = 3, url = MAIN_URL):
    h = []
    response = requests.get(url)
    soup = BeautifulSoup(response.text, features='lxml')
    tag_last_news = soup.find('div', attrs={'class': 'mb-25'})
    s = 0
    for tags in tag_last_news.find_all('a', attrs={'class': 'news-lenta'}):
        s += 1
        h.append(tags.attrs['href'])
        if s >= MAX_NUMBER:
            break
    return h



def parse_popular_news(url = MAIN_URL + '/news/list?f=top', max_number = 3) -> list:
    h = []
    browser = webdriver.Chrome('Desktop/chromedrive')
    browser.get(url)
    element = browser.find_element_by_id('top-news-content')
    html = element.get_attribute('innerHTML')
    soup = BeautifulSoup(html, features='lxml')
    s = 0
    for tags in soup.find_all('a', {'class':'news-recommended'}):
        s += 1
        h.append(MAIN_URL + tags.attrs['href'])
        if s >= max_number:
            break
    return h

print(parse_popular_news())


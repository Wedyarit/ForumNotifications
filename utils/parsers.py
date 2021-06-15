import bs4
import requests

from utils.topic import Topic


def questions():
    soup = bs4.BeautifulSoup(requests.get('https://forum.excalibur-craft.ru/forum/11-i/').text, 'html.parser').select('#ipsLayout_mainArea > div:nth-child(2) > div.ipsBox.ipsResponsive_pull')[0]
    data = soup.find_all('li', {'class': 'ipsDataItem cForumQuestion'})[5]
    return Topic(title=data.find_all('a')[0]['title'], author=data.find_all('a')[1].text, url=data.find_all('a')[0]['href'], date=data.find('time')['title'], date_last=data.find('time')['data-short'])


def support():
    soup = bs4.BeautifulSoup(requests.get('https://forum.excalibur-craft.ru/forum/41-i/').text, 'html.parser').select('#ipsLayout_mainArea > div:nth-child(2) > div.ipsBox.ipsResponsive_pull')[0]
    data = soup.find_all('li', {'class': 'ipsDataItem cForumQuestion'})[8]
    return Topic(title=data.find_all('a')[0]['title'], author=data.find_all('a')[1].text, url=data.find_all('a')[0]['href'], date=data.find('time')['title'], date_last=data.find('time')['data-short'])

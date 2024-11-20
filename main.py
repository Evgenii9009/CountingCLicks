import requests
from urllib.parse import urlparse
access_token = '828b3c53828b3c53828b3c53d681af20b28828b828b3c53e5bc01f8d674ab8b73122beb'

def shorten_link(access_token, link):
    headers = {
        "Authorization": f"Bearer {access_token}"
        }
    params = {
        "v": 5.199,
        "url": link
        }
    service_url = 'https://api.vk.ru/method/utils.getShortLink'
    response = requests.get(service_url, params=params, headers=headers)
    response.raise_for_status()
    short_link = response.json()['response']['short_url']
    print("Сокращённая ссылка:", short_link)
    return short_link

def count_clicks(access_token, link):
    replaced_link = link.replace("https://vk.cc/", "")
    headers = {
        "Authorization": f"Bearer {access_token}"
        }
    params = {
        "v": 5.199,
        "key": replaced_link,
        "interval": 'forever',
        }
    service_url = "https://api.vk.ru/method/utils.getLinkStats"
    response = requests.get(service_url, params=params, headers=headers)
    response.raise_for_status()
    counted_clicks = response.json()["response"]["stats"][0]['views']
    print("Количество кликов:", counted_clicks)
    return counted_clicks

def is_shorten_link(link):
    parsed = urlparse(link)
    #scheme = parsed.scheme
    #netloc = parsed.netloc
    beginning = parsed.scheme+"://"+parsed.netloc+"/"
    if beginning == "https://vk.cc/":
        count_clicks(access_token, link)
    else:
        shorten_link(access_token, link)
#try:
#  short_link = shorten_link(access_token, input("Введите ссылку: ",))
#except KeyError:
#  print("Введена неправильная ссылка!") # если ошибка
#try:
#  counted_clicks = count_clicks(access_token, input("Введите ссылку: ",))
#except KeyError:
#  print("Введена неправильная ссылка!") # если ошибка
is_shorten_link(input('Введите ссылку: ',))

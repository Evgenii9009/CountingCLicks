import requests
import os


from urllib.parse import urlparse
from dotenv import load_dotenv
load_dotenv()

ACCESS_TOKEN = os.environ['ACCESS_TOKEN']


def shorten_link(ACCESS_TOKEN, link):
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    params = {
        "v": 5.199,
        "url": link
        }
    service_url = 'https://api.vk.ru/method/utils.getShortLink'
    response = requests.get(service_url, params=params, headers=headers)
    short_link = response.json()['response']['short_url']
    return short_link


def count_clicks(ACCESS_TOKEN, link):
    replaced_link = link.replace("https://vk.cc/", "")
    headers = {
        "Authorization": f"Bearer {ACCESS_TOKEN}"
        }
    params = {
        "v": 5.199,
        "key": replaced_link,
        "interval": 'forever',
        }
    service_url = "https://api.vk.ru/method/utils.getLinkStats"
    response = requests.get(service_url, params=params, headers=headers)
    counted_clicks = response.json()["response"]["stats"][0]['views']
    return counted_clicks


def is_shorten_link(link):
    parsed = urlparse(link)
    beginning = parsed.scheme+"://"+parsed.netloc+"/"
    if beginning == "https://vk.cc/":
        counted_clicks = count_clicks(ACCESS_TOKEN, link)
        return counted_clicks
    else:
        short_link = shorten_link(ACCESS_TOKEN, link)
        return short_link


def main():
    try:
        result = is_shorten_link(input("Введите ссылку: "))
        if  isinstance(result, int):
            print("Количество кликов:", result)
        else:
            print("Сокращённая ссылка: ", result)
    except KeyError:
        print("Введена неправильная ссылка!")


if __name__ == "__main__":
    main()

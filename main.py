import requests
import sys
import os
import argparse


from dotenv import load_dotenv


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument ('--name', default='https://vk.cc/cx80Y1')
    return parser


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
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    else:
        short_link = decoded_response['response']['short_url']
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
    decoded_response = response.json()
    if 'error' in decoded_response:
        raise requests.exceptions.HTTPError(decoded_response['error'])
    else:
        counted_clicks = decoded_response["response"]["stats"][0]['views']
        return counted_clicks


def is_shorten_link(access_token, link):
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
    decoded_response = response.json()
    return 'error' not in decoded_response



def main():
    load_dotenv()
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])
    access_token = os.getenv('VKAPI_TOKEN')
    try:
        user_input = str(namespace.name)
        if is_shorten_link(access_token, user_input):
            counted_clicks = count_clicks(access_token, user_input)
            print("Количество кликов:", counted_clicks)
        else:
            short_link = shorten_link(access_token, user_input)
            print("Сокращённая ссылка: ", short_link)
    except requests.exceptions.HTTPError:
        print("Введена неправильная ссылка!")


if __name__ == "__main__":
    main()

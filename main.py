import requests
import os


from dotenv import load_dotenv


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
    decoded_response = response.json()
    if 'error' in decoded_response:
        return False
    else:
        return True


def main():
    load_dotenv("/home/eugene/DEVMAN_TASKS/CountingCLicks/.env.token")
    ACCESS_TOKEN = os.environ['VKAPI_TOKEN']
    try:
        user_input = input("Введите ссылку: ")
        if is_shorten_link(ACCESS_TOKEN, user_input):
            counted_clicks = count_clicks(ACCESS_TOKEN, user_input)
            print("Количество кликов:", counted_clicks)
        else:
            short_link = shorten_link(ACCESS_TOKEN, user_input)
            print("Сокращённая ссылка: ", short_link)
    except requests.exceptions.HTTPError:
        print("Введена неправильная ссылка!")


if __name__ == "__main__":
    main()

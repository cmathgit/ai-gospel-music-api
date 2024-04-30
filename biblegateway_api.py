import requests

base_url = 'https://www.biblegateway.com/votd/get/?format=JSON'

    # King James Version = 9
def get_bible_votd_kjv():
    url = f"{base_url}&version=9"
    response = requests.get(url)
    return response.json()


    # Amplified Bible = 45
def get_bible_votd_amp():
    url = f"{base_url}&version=45"
    response = requests.get(url)
    return response.json()


    # The Message = 65
def get_bible_votd_msg():
    url = f"{base_url}&version=65"
    response = requests.get(url)
    return response.json()
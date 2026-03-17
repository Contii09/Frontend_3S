import requests
from django.urls import get_urlconf

base_url = "https://api.thecatapi.com/v1"


def get_gatos():
    url = f"{base_url}/breeds"

    headers = {
        "xx-api-key": "live_W363SW9EVlx7SYbrZielBRfM8GWSkwryd4yiUZktaYi7DpRigMfhNvyDcz17C7nU",
    }

    resposta = requests.get(url, headers=headers)

    return resposta.json()

def get_image():
    url = "https://api.thecatapi.com/v1/images/search"

    resposta = requests.get(url)

    return resposta.json()[0]

import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def get_litress(url, **kwargs):
    base_url = "https://api.litres.ru/foundation/api/"
    with step(f"GET {url}"):
        response = requests.get(base_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        print(f"/n {response.request}")
    return response


def post_litress(url, **kwargs):
    base_url = "https://api.litres.ru/foundation/api/"
    with step(f"POST {url}"):
        response = requests.post(base_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        print(f"/n {response.request}")
    return response


def put_litress(url, **kwargs):
    base_url = "https://api.litres.ru/foundation/api/"
    with step(f"PUT {url}"):
        response = requests.put(base_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
        print(f"/n {response.request}")
    return response

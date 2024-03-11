import logging

import allure
import curlify
import requests
from allure_commons._allure import step
from allure_commons.types import AttachmentType


def request_litres(base_url, method, url, **kwargs):

    with step(f"{method} {url}"):
        if method == 'GET':
            response = requests.get(base_url + url, **kwargs)
        elif method == 'POST':
            response = requests.post(base_url + url, **kwargs)
        elif method == 'PUT':
            response = requests.put(base_url + url, **kwargs)
        curl = curlify.to_curl(response.request)
        logging.info(curl)
        allure.attach(body=curl, name="curl", attachment_type=AttachmentType.TEXT, extension="txt")
    return response




import json
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
        allure.attach(body=curl,
                      name="curl",
                      attachment_type=AttachmentType.TEXT,
                      extension="txt")
        allure.attach(body=json.dumps(response.json(),
                                      indent=4,
                                      ensure_ascii=True),
                      name="Response",
                      attachment_type=AttachmentType.JSON,
                      extension="json")
        logging.info(response.request.url)
        logging.info(response.status_code)
        logging.info(response.text)
    return response




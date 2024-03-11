import os

from dotenv import load_dotenv

from litres_project import utils

load_dotenv(dotenv_path=utils.file.abs_path_from_project('.env.credentials'))
login: str = os.getenv("USER_LOGIN")
password: str = os.getenv("USER_PASSWORD")
wrong_login: str = os.getenv("WRONG_LOGIN")
wrong_password: str = os.getenv("WRONG_PASSWORD")

BASE_URL = "https://api.litres.ru/foundation/api/"
ADD_TO_CART_URL = "/cart/arts/add"
CART_URL = '/cart/status'
AUTH_URL = "/auth/login"
SEARCH_URL = 'search/suggestions'
LOGIN_AVAILABLE_URL = "/auth/login-available"

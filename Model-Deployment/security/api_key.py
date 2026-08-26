import os


API_KEY = os.getenv("API_KEY")


def validate_api_key(request_key):

    if not API_KEY:
        return False

    return request_key == API_KEY

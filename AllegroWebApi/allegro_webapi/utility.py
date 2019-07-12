import requests
import time

REST = '../AllegroREST/AllegroREST/'


class NetworkError(RuntimeError):
    pass


def retryer(func):
    retry_on_exceptions = (
        requests.exceptions.Timeout,
        requests.exceptions.ConnectionError,
        requests.exceptions.HTTPError
    )
    max_retries = 10
    timeout = 5

    def inner(*args, **kwargs):
        for i in range(max_retries):
            try:
                result = func(*args, **kwargs)
            except retry_on_exceptions:
                time.sleep(timeout)
                continue
            else:
                return result
        else:
            raise NetworkError

    return inner

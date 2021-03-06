import requests

from ..config import USER_AGENT


def notify(title,
           message,
           key,
           retcode=None):
    """
    Required paramter:
        * ``key`` - The Simplepush identification key, created by
        installing the Android App (https://simplepush.io)
    """

    data = {
        'title': title if len(title) <= 20 else title[:19] + u'\u2026',
        'msg': message,
        'key': key
    }

    headers = {'User-Agent': USER_AGENT}

    endpoint = "https://api.simplepush.io"

    resp = requests.post(endpoint + '/send',
                         data=data,
                         headers=headers)

    resp.raise_for_status()

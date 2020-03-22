import requests
import json
from urllib.parse import urlencode


url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'
auth_key = 'trnsl.1.1.20200321T131833Z.751fc8fe0c12f0d0.d7007fb280b90f86676cdebf291b157a9747bf2e'

def translater(key, lang, text):
    params = {'key': key,
            'lang': lang,
            'text': text}
    path = '?'.join((url, urlencode(params)))
    response = requests.get(path)
    return response.json()

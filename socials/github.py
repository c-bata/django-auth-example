import requests
import json

from django.conf import settings


def get_github_user_info(access_token):
    url = "https://api.github.com/user?access_token={token}".format(token=access_token)
    res = requests.get(url)
    return res.json()


def get_access_token(request):
    code = request.GET['code']
    payload = {
        "client_id": settings.SOCIAL_AUTH_GITHUB_KEY,
        "client_secret": settings.SOCIAL_AUTH_GITHUB_SECRET,
        "code": code,
    }
    headers = {'Content-Type': 'application/json'}
    res = requests.post('https://github.com/login/oauth/access_token',
                        data=json.dumps(payload), headers=headers)
    if res.status_code != 200:
        raise Exception("Github authentication error")
    res_params = {k: v for k, v in
                  [p.split('=') for p in res.text.split('&')]}
    return res_params['access_token']

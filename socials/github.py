import requests
import json

from django.db.models import fields
from django.contrib.auth import get_user_model

from socials.models import Social

UserModel = get_user_model()


def get_or_create_user(nickname, provider, uid, email):
    try:
        social = Social.objects.get(provider=provider, uid=uid)
        return social.user
    except Social.DoesNotExist:
        social = Social(provider=provider, uid=uid)

    if email is None:
        email = "noregister@example.com"

    user = UserModel(
        username=nickname, email=email,
        password=UserModel.objects.make_random_password(),
    )
    user.save()
    social.user = user
    social.save(force_insert=True)
    return user


def get_github_user_info(access_token):
    url = "https://api.github.com/user?access_token={token}".format(token=access_token)
    res = requests.get(url)
    return res.json()


def get_access_token(payload):
    headers = {'Content-Type': 'application/json'}
    res = requests.post('https://github.com/login/oauth/access_token',
                        data=json.dumps(payload), headers=headers)
    if res.status_code != 200:
        raise Exception("Github authentication error")
    res_params = {k: v for k, v in
                  [p.split('=') for p in res.text.split('&')]}
    return res_params['access_token']

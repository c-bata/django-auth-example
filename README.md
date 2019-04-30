django-auth-example
===================

Sample source code for my talk (title: "Djangoの認証処理実装パターン" in Japanese) at [Django Congress JP 2018](https://djangocongress.jp/).
In this talk, I introduced how to implement some authentication patterns in django.

* [PR Email/Password authentication built on custom authentication backend.](https://github.com/c-bata/django-auth-example/pull/2)
* [PR How to define custom user model from AbstractBaseUser.](https://github.com/c-bata/django-auth-example/pull/3)
* [PR Social authentication using social-auth-core.](https://github.com/c-bata/django-auth-example/pull/1)
* [PR Social authentication from scratch (There is no dependency with social-auth-core).](https://github.com/c-bata/django-auth-example/pull/4)

## Requirements

* Python 3.7
* Django 2.2
* And others listed in requirements.txt

## Setup databases using Docker and Run application on local machine

```sh
# django
export DJ_SECRET_KEY=secretkey
export DJ_DEBUG=True

# social-auth
export SOCIAL_AUTH_GITHUB_KEY=xxxxxxxxxxxxxxxxxxxx
export SOCIAL_AUTH_GITHUB_SECRET=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
```

Running:

```console
$ pip -c requirements/constraints.txt install -r requirements/develop.txt
$ python manage.py migrate
$ python manage.py insert_dummy_data
$ python manage.py runserver
```

## Branch structures

* `master`: The project on master branch customizing User model, supporting Github OAuth.
* `base`: Base branch to see the changes of each Pull Requests to describe following features.
    * `email-auth-backend`: Email/Password authentication built on custom authentication backend.
    * `customize-user-model`: How to define custom user model from AbstractBaseUser.
    * `django-social-auth`: Social authentication using social-auth-core.
    * `github-oauth-from-scratch`: Social authentication from scratch (There is no dependency with social-auth-core).

# License

This software is released under the MIT License, see LICENSE.txt.

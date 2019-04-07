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

## Using Docker compose

```console
$ docker-compose build
$ docker-compose up -d
$ docker-compose run backend python manage.py migrate
```

Other commands:

* bash: `docker-compose exec backend /bin/bash`
* logs: `docker-compose logs -f backend`
* mysql: `docker-compose exec mysql /bin/bash` and `mysql -u root`

Custom management commands:

* Inserting dummy ata: `python manage.py insert_dummy data`
* Load testing: `python manage.py load_test`


## Setup databases using Docker and Run application on local machine

```sh
# django
export SECRET_KEY=secretkey

# database
export REDIS_PASSWORD=redispass
export MYSQL_USER=snippets
export MYSQL_PASSWORD=mysqlpass
export MYSQL_DATABASE=snippets

# social-auth
export SOCIAL_AUTH_GITHUB_KEY=xxxxxxxxxxxxxxxxxxxx
export SOCIAL_AUTH_GITHUB_SECRET=yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy
```

Running:

```console
$ docker-compose up -d mysql redis
$ pip -c requirements/constraints.txt install -r requirements/develop.txt
$ python manage.py migrate
$ python manage.py runserver
```

## Branch structures

* `master`: The project on master branch customized User model, 
* `base`: Base branch to see the changes of each Pull Requests to describe following features.
    * `email-auth-backend`: Email/Password authentication built on custom authentication backend.
    * `customize-user-model`: How to define custom user model from AbstractBaseUser.
    * `django-social-auth`: Social authentication using social-auth-core.
    * `github-oauth-from-scratch`: Social authentication from scratch (There is no dependency with social-auth-core).

# License

This software is released under the MIT License, see LICENSE.txt.

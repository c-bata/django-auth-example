from django.conf import settings


def social_login_url(request):
    return {
        'GITHUB_LOGIN_URL': f"https://github.com/login/oauth/authorize?client_id={ settings.SOCIAL_AUTH_GITHUB_KEY }",
    }

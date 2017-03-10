from __future__ import unicode_literals

from django.conf import settings
import requests
from requests.auth import AuthBase

from .models import User


class BearerTokenAuth(AuthBase):
    def __init__(self, access_token):
        self._access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer {}".format(self._access_token)
        return r



class JLMOAuth2(object):
    PROFILE_URL = "https://auth.jlm2017.fr/voir_profil"

    def authenticate(self, access_token=None):
        if access_token:
            res = requests.get(settings.PROFILE_URL, auth=BearerTokenAuth(access_token))

            if res.status_code // 100 == 2:
                try:
                    profile = res.json()
                except ValueError:
                    # it was not JSON
                    return None

                email = profile.get('email', None)
                if email:
                    user, created = User.objects.get_or_create(email=email)
                    return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

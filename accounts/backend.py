from __future__ import unicode_literals

from django.conf import settings
import requests
from requests.auth import AuthBase

from .models import User
from .actions.profile import extract_profile, update_profile


class BearerTokenAuth(AuthBase):
    def __init__(self, access_token):
        self._access_token = access_token

    def __call__(self, r):
        r.headers['Authorization'] = "Bearer {}".format(self._access_token)
        return r


class JLMOAuth2(object):
    def authenticate(self, access_token=None):
        if access_token:
            res = requests.get(settings.PROFILE_URL, auth=BearerTokenAuth(access_token))

            if res.status_code // 100 == 2:
                try:
                    jlm_profile = res.json()
                except ValueError:
                    # it was not JSON
                    return None

                pk = jlm_profile.get('id', None)
                profile = extract_profile(jlm_profile)

                if id:
                    user, created = User.objects.get_or_create(pk=pk, defaults=profile)

                    if not created:
                        update_profile(user, profile)
                    return user

            # not authenticated
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

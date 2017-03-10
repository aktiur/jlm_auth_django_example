from django.conf import settings
from django.views.generic import RedirectView
from django.urls import reverse_lazy
from django.utils.translation import string_concat
from django.utils.crypto import get_random_string
from django.http import HttpResponseBadRequest

from django.contrib.auth import authenticate, login

import logging

logger = logging.getLogger(__name__)

from oauth2client.client import OAuth2WebServerFlow

flow = OAuth2WebServerFlow(
    client_id=settings.CLIENT_ID,
    client_secret=settings.CLIENT_SECRET,
    scope=settings.DEFAULT_SCOPE,
    auth_uri=settings.AUTHORIZATION_URL,
    token_uri=settings.ACCESS_TOKEN_URL,
    redirect_uri=string_concat(settings.REDIRECT_BASE, reverse_lazy('accounts:oauth_callback'))
)


class RedirectToAuthProvider(RedirectView):
    http_method_names = ['get']

    def get_redirect_url(self, *args, **kwargs):

        state_nonce = get_random_string(32)

        self.request.session['oauth2_nonce'] = state_nonce
        return flow.step1_get_authorize_url(state=state_nonce)


class AuthReturn(RedirectView):
    http_method_names = ['get']
    url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        state_nonce = request.session.get('oauth2_nonce', None)
        if not state_nonce or request.GET.get('state') != state_nonce:
            return HttpResponseBadRequest(b'Bad state')

        credentials = flow.step2_exchange(request.GET)
        access_token = credentials.get_access_token().access_token

        user = authenticate(access_token=access_token)

        if user:
            user.access_token = access_token
            user.save()
            login(request, user)
        else:
            return HttpResponseBadRequest(b'Did not get profile')

        # delete nonce so that the redirect cannot be done twice
        del request.session['oauth2_nonce']

        return super(AuthReturn, self).get(request, *args, **kwargs)

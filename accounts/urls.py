from django.conf.urls import url
from django.contrib.auth.views import logout

from . import views

urlpatterns = [
    # the view responsible for redirecting the user TO the OAuth provider
    url(r'^connexion/$', views.RedirectToAuthProvider.as_view(), name='connexion'),
    # the view that will handle the redirect FROM the OAuth provider
    url(r'^connexion/retour$', views.AuthReturn.as_view(), name='oauth_callback'),
    # standard disconnection view
    url(r'^deconnexion/$', logout, {'next_page': 'index'}, name='deconnexion')
]

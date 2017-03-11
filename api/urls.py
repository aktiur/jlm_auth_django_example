from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^token$', views.ObtainJsonWebToken.as_view(), name='token'),
    url(r'^profil$', views.UserView.as_view(), name='profil'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^profil$', views.UserView.as_view(), name='profil'),
]

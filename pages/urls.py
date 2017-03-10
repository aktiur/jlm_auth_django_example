from django.conf.urls import url

from . import views

urlpatterns = [
    url('', views.MainPage.as_view(), name='index'),
]

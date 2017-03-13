from __future__ import unicode_literals

from django.views.generic import TemplateView


class MainPage(TemplateView):
    http_method_names = ['get']
    template_name = 'pages/main_page.html'

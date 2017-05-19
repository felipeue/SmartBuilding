from main.models import Building
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, TemplateView


class IndexView(TemplateView):
    template_name = "home.html"


class LoginView(TemplateView):
    template_name = "login.html"






from django.views.generic import TemplateView, RedirectView
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render
from main.permissions import *


class IndexView(TemplateView):
    template_name = "home.html"


def login_resident(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                if user.concierge:
                    return HttpResponseRedirect('/concierge/dashboard/')
                elif user.owner:
                    return HttpResponseRedirect('/owner/dashboard/')
                elif user.resident:
                    return HttpResponseRedirect('/resident/dashboard/')
                else:
                    return HttpResponseRedirect('/logout/')
            else:
                return HttpResponseRedirect('/login/')
        else:
            return HttpResponseRedirect('/login/')
    else:
        return render(request, 'login/login_owner.html', {})


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)




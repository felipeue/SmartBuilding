from django.views.generic import TemplateView, FormView, RedirectView
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from main.permissions import *


class IndexView(TemplateView):
    template_name = "home.html"


class LoginView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("dashboard")

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return HttpResponseRedirect(self.get_success_url())
        else:
            return super(LoginView, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        login(self.request, form.get_user())
        return super(LoginView, self).form_valid(form)


class LogoutView(RedirectView):
    pattern_name = 'login'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(request, *args, **kwargs)


class DashboardView(OwnerLoginRequiredMixin, TemplateView):
    template_name = "index.html"


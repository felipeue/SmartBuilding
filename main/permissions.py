from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from main.models import *


class OwnerLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("login"))
        elif not Owner.objects.filter(user_origin=request.user).exists():
            return HttpResponseRedirect(reverse_lazy("logout"))
        else:
            return super(OwnerLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ConciergeLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("login"))
        elif not Concierge.objects.filter(userOrigin=request.user).exists():
            return HttpResponseRedirect(reverse_lazy("logout"))
        else:
            return super(ConciergeLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ResidentLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("login"))
        elif not Resident.objects.filter(userOrigin=request.user).exists():
            return HttpResponseRedirect(reverse_lazy("logout"))
        else:
            return super(ResidentLoginRequiredMixin, self).dispatch(request, *args, **kwargs)
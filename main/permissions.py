from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect


class OwnerLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("login"))
        elif not request.user.profile.is_owner:
            return HttpResponseRedirect(reverse_lazy("logout"))
        else:
            return super(OwnerLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ConciergeLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("login"))
        elif not request.user.profile.is_concierge:
            return HttpResponseRedirect(reverse_lazy("logout"))
        else:
            return super(ConciergeLoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class ResidentLoginRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated():
            return HttpResponseRedirect(reverse_lazy("login"))
        elif not request.user.profile.is_resident:
            return HttpResponseRedirect(reverse_lazy("logout"))
        else:
            return super(ResidentLoginRequiredMixin, self).dispatch(request, *args, **kwargs)
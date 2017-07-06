from django.views.generic import TemplateView
from main.permissions import OwnerLoginRequiredMixin
# Create your views here.


class DashboardView(OwnerLoginRequiredMixin, TemplateView):
    template_name = "index_dashboard.html"

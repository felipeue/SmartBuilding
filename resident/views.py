from django.views.generic import TemplateView
from main.permissions import ResidentLoginRequiredMixin


class DashboardView(ResidentLoginRequiredMixin, TemplateView):
    template_name = "index_dashboard.html"

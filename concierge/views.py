from django.views.generic import TemplateView
from main.permissions import ConciergeLoginRequiredMixin
# Create your views here.


class DashboardView(ConciergeLoginRequiredMixin, TemplateView):
    template_name = "index_dashboard.html"

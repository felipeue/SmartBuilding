from django.conf.urls import url
from owner import views


urlpatterns = [
    url(r'^dashboard/$',
        views.DashboardView.as_view(),
        name='dashboard_owner'),
    ]

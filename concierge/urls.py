from django.conf.urls import url
from concierge import views
from django.contrib.auth import views as auth_views


urlpatterns = [
    url(r'^dashboard/$',
        views.DashboardView.as_view(),
        name='dashboard_concierge'),
    ]

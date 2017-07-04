from django.conf.urls import url
from main import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^$',
        views.IndexView.as_view()),
    url(r'^login/$',
        views.LoginView.as_view(),
        name='login'),
    url(r'^dashboard/$',
        views.DashboardView.as_view(),
        name='dashboard'),
    url(r'^logout/$',
        views.LogoutView.as_view(),
        name='logout'),
    url(r'^password_reset/$',
        auth_views.password_reset,
        {'template_name': 'login/password_reset.html'},
        name='password_reset'),
    url(r'^password_reset/done/$',
        auth_views.password_reset_done,
        {'template_name': 'login/password_reset_done.html'},
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        auth_views.password_reset_confirm,
        {'template_name': 'login/password_reset_confirm.html'},
        name='password_reset_confirm'),
    url(r'^reset/done/$',
        auth_views.password_reset_complete,
        {'template_name': 'login/password_reset_complete.html'},
        name='password_reset_complete'),
    ]

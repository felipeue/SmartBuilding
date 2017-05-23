from django.conf.urls import url
from main import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
    url(r'^login/$', views.LoginView.as_view(), name='login'),
    url(r'^dashboard/$', views.DashboardView.as_view(), name='dashboard'),
    url(r'^logout/$', views.LogoutView.as_view(), name='logout'),
]

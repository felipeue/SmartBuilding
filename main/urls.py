from django.conf.urls import url
from main import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^$', views.IndexView.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.moods),
    # url(r'^(?P<year>\d{4})-(?P<month>\d{2})-(?P<day>\d{2})', views.mood),
    url(r'^mood', views.MoodList.as_view()),
]
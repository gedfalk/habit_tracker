from django.urls import path
from . import views

app_name = 'tracker'

urlpatterns = [
    path('', views.tracker_calendar, name='tracker_calendar'),
]
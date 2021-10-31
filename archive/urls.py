from django.urls import path
from . import views

app_name = 'archive'

urlpatterns = [
    path('', views.session_list, name='session_list'),
]
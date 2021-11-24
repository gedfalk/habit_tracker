from django.urls import path
from django.urls.resolvers import URLPattern
from . import views

app_name = 'sessions'

urlpatterns = [
    path('sessions/', views.SessionListView.as_view(), name='session_list'),
]
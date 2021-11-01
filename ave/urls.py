from django.urls import path
from . import views

app_name = 'ave'

urlpatterns = [
    path('', views.ave, name='ave')
]
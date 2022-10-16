from django import views
from django.urls import path
from . import views

app_name = 'data_surat'
urlpatterns = [
    path('', views.index, name='index')
]

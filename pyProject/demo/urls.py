from django.urls import path
from . import views
urlpatterns = [
path('', views.demo_show, name = 'demo_show'),
]
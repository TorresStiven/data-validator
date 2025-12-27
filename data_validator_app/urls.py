from django.urls import path
from data_validator_app import views

urlpatterns = [
    path('', views.home, name='home'),
]
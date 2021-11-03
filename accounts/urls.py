from django.urls import path
from accounts import views

urlpatterns = [
    path('', views.account_settings, name='account_settings'),
]

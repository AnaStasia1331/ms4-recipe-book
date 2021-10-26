from django.urls import path
from recipes import views

urlpatterns = [
    path('', views.get_recipes, name='get_recipes'),
]

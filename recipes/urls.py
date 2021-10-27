from django.urls import path
from recipes import views

urlpatterns = [
    path('get/', views.get_recipes, name='get_recipes'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/', views.edit_recipe, name='edit_recipe'),
    path('view/', views.view_recipe, name='view_recipe'),
]

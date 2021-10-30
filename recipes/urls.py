from django.urls import path
from recipes import views

urlpatterns = [
    path('get/', views.get_recipes, name='get_recipes'),
    path('add/', views.add_recipe, name='add_recipe'),
    path('edit/<int:recipe_id>', views.edit_recipe, name='edit_recipe'),
    path('view/<int:recipe_id>', views.view_recipe, name='view_recipe'),
    path('delete/<int:recipe_id>', views.delete_recipe, name='delete_recipe'),
]

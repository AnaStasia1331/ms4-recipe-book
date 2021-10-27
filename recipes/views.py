from django.shortcuts import render

# Create your views here.


def get_recipes(request):
    return render(request, 'recipes/all_recipes.html')


def add_recipe(request):
    return render(request, 'recipes/add_recipe.html')

from django.shortcuts import render
from .models import Recipe, Course

# Create your views here.


def get_recipes(request):
    """ A view to show all recipes """

    recipes = Recipe.objects.all()

    context = {
        'recipes': recipes,
    }

    return render(request, 'recipes/all_recipes.html', context)


def add_recipe(request):
    """ A view to add a new recipe """

    courses = Course.objects.all()

    context = {
        'courses': courses,
    }

    return render(request, 'recipes/add_recipe.html', context)


def edit_recipe(request):
    return render(request, 'recipes/edit_recipe.html')


def view_recipe(request):
    return render(request, 'recipes/view_recipe.html')

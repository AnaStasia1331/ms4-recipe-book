from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Recipe, Course
from .forms import AddRecipeForm

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

    if request.method == 'POST':
        form = AddRecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added recipe!')
            return redirect('get_recipes')
        else:
            messages.error(request,
                       ('Failed to add recipe. Please ensure the form is valid.'))
    else:
        form = AddRecipeForm()

    courses = Course.objects.all()
    
    context = {
        'courses': courses,
        'form': form,
    }

    return render(request, 'recipes/add_recipe.html', context)


def edit_recipe(request):
    return render(request, 'recipes/edit_recipe.html')


def view_recipe(request):
    return render(request, 'recipes/view_recipe.html')

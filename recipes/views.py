from django.shortcuts import render
from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib import messages
from .models import Recipe, Course
from .forms import RecipeForm

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
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully added recipe!')
            return redirect('get_recipes')
        else:
            messages.error(request,
                       ('Failed to add the recipe. Please ensure the form is valid.'))
    else:
        form = RecipeForm()

    courses = Course.objects.all()
    
    context = {
        'courses': courses,
        'form': form,
    }

    return render(request, 'recipes/add_recipe.html', context)


def edit_recipe(request, recipe_id):
    """Edit a recipe selected from All Recipes page"""

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated recipe!')
            return redirect('get_recipes')
        else:
            messages.error(request,
                           ('Failed to update the recipe. '
                            'Please ensure the form is valid.'))
    else:
        form = RecipeForm(instance=recipe)
        messages.info(request, f'You are editing {recipe.recipe_name}')

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/edit_recipe.html', context)


def view_recipe(request, recipe_id):
    """View a recipe selected from All Recipes page"""

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/view_recipe.html', context)

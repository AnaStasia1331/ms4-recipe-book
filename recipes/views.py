from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .models import Recipe, Course
from .forms import RecipeForm
from django.db.models import Q

# Create your views here.


def get_recipes(request):
    """ A view to show all recipes that belongs to logged in user, with search queries and filtering """
    recipes = Recipe.objects.filter(user=request.user)
    query = None
    course = None

    # Source: Code Institute Project - Boutique Ado
    if 'course' in request.GET:
        course = request.GET['course'].split(',')
        recipes = recipes.filter(course__course_choice__in=course)
        course = Course.objects.filter(course_choice__in=course)

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                return redirect(reverse('get_recipes'))
            
            queries = Q(recipe_name__icontains=query) | Q(course__course_choice__icontains=query)
            recipes = recipes.filter(queries)

    context = {
        'recipes': recipes,
        'search_term': query,
        'selected_course': course,
    }

    return render(request, 'recipes/my_recipes.html', context)


def add_recipe(request):
    """ A view to add a new recipe """
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
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


def delete_recipe(request, recipe_id):
    """Delete a recipe selected from All Recipes page"""

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()

    return redirect('get_recipes')

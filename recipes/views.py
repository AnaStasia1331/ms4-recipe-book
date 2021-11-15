from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages

from accounts.models import UserAccount
from .models import Recipe, Course
from .forms import RecipeForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.


@login_required
def get_recipes(request):
    """A view to show all recipes that belongs to
    logged in user, with search queries and filtering"""
    query = None
    course = None

    # Source: Code Institute Project - Boutique Ado
    if 'course' in request.GET:
        course = request.GET['course'].split(',')
        recipes = Recipe.objects.filter(
            course__course_choice__in=course, user=request.user)
        course = Course.objects.filter(course_choice__in=course)
    elif request.GET and request.GET['q']:
        query = request.GET['q']
        queries = Q(recipe_name__icontains=query) | Q(
            course__course_choice__icontains=query)
        recipes = Recipe.objects.filter(queries, user=request.user)
    else:
        recipes = Recipe.objects.filter(user=request.user)

    if Recipe.objects.filter(user=request.user).count() > 0:
        has_recipes = True
    else:
        has_recipes = False

    context = {
        'recipes': recipes,
        'has_recipes': has_recipes,
        'search_term': query,
        'selected_course': course,
    }

    return render(request, 'recipes/my_recipes.html', context)


@login_required
def add_recipe(request):
    """ A view to add a new recipe """
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = RecipeForm(request.POST, request.FILES)
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()
                return redirect('get_recipes')
            else:
                messages.error(request,
                               ('Failed to add the recipe. '
                                'Please ensure the form is valid.'))
    else:
        form = RecipeForm()

    courses = Course.objects.all()
    # On the 4th recipe creation, the modal window will be displayed
    # asking to make a payment for the website.
    recipe_count = Recipe.objects.filter(user=request.user).count()

    try:
        account = UserAccount.objects.get(user=request.user)
        has_paid = account.has_paid
    except UserAccount.DoesNotExist:
        has_paid = False
    context = {
        'courses': courses,
        'form': form,
        'recipe_count': recipe_count,
        'has_paid': has_paid,
    }

    return render(request, 'recipes/add_recipe.html', context)


@login_required
def edit_recipe(request, recipe_id):
    """Edit a recipe selected from All Recipes page"""

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()
            messages.success(request,
                           ('Failed to update the recipe. '
                            'Please ensure the form is valid.'))
            # return redirect('get_recipes')
        else:
            messages.error(request,
                           ('Failed to update the recipe. '
                            'Please ensure the form is valid.'))
    else:
        form = RecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/edit_recipe.html', context)


@login_required
def view_recipe(request, recipe_id):
    """View a recipe selected from All Recipes page"""

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    form = RecipeForm(instance=recipe)

    context = {
        'form': form,
        'recipe': recipe,
    }

    return render(request, 'recipes/view_recipe.html', context)


@login_required
def delete_recipe(request, recipe_id):
    """Delete a recipe selected from All Recipes page"""

    recipe = get_object_or_404(Recipe, pk=recipe_id)
    recipe.delete()

    return redirect('get_recipes')

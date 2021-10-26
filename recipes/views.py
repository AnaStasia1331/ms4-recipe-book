from django.shortcuts import render

# Create your views here.


def get_recipes(request):
    return render(request, 'recipes/all_recipes.html')

from django import forms
from .models import Recipe


class AddRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = ('course', 'recipe_name', 'ingredients', 'steps', 'preparation_time', 'image')


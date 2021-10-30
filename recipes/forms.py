from django import forms
from .models import Recipe
from django.forms import Select, Textarea, TextInput


class AddRecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'course', 'recipe_name', 'ingredients',
            'steps', 'preparation_time', 'image']
        widgets = {
            'recipe_name': TextInput(attrs={
                'class': "form-control",
                'style': 'max-length: 50;'
            }),
            'course': Select(attrs={
                'class': "form-select",
            }),
            'ingredients': Textarea(attrs={
                'class': "form-control",
            }),
            'steps': Textarea(attrs={
                'class': "form-control",
            }),
            'preparation_time': TextInput(attrs={
                'class': "form-control",
                'type': "time",
            }),
            'image': TextInput(attrs={
                'id': "image",
                'class': "form-control filestyle",
                'type': "file",
            }),
        }
        

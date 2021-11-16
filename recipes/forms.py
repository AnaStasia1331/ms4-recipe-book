from django import forms
from .models import Recipe
from django.forms import Select, Textarea, TextInput, FileInput


class RecipeForm(forms.ModelForm):

    class Meta:
        model = Recipe
        fields = [
            'course', 'recipe_name', 'ingredients',
            'steps', 'preparation_time', 'image']
        widgets = {
            'recipe_name': TextInput(attrs={
                'class': 'form-control',
                'style': 'max-length: 50;',
                'required': True,
                'oninvalid': "this.setCustomValidity('Please fill in the recipe name field.')",
                'oninput': "this.setCustomValidity('')"
            }),
            'course': Select(attrs={
                'class': "form-select",
                'style': 'text-transform: capitalize;'
            }),
            'ingredients': Textarea(attrs={
                'class': 'form-control',
            }),
            'steps': Textarea(attrs={
                'class': 'form-control',
            }),
            'preparation_time': TextInput(attrs={
                'class': 'form-control',
                'type': 'time',
            }),
            'image': FileInput(attrs={
                'id': 'id_image',
                'class': 'form-control filestyle',
            }),
        }

    def __init__(self, *args, **kwargs):
        super(RecipeForm, self).__init__(*args, **kwargs)
        # to get rid of the empty course dropdown value,
        # set empty_label to None
        self.fields['course'].empty_label = None

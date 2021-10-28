from django.contrib import admin
from .models import Recipe, Course

# Register your models here.


class RecipeAdmin(admin.ModelAdmin):
    list_display = (
        'course',
        'recipe_name',
        'ingredients',
        'steps',
        'preparation_time',
        'image',
    )

    ordering = ('recipe_name',)


class CourseAdmin(admin.ModelAdmin):
    list_display = (
        'course_choice',
    )


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Course, CourseAdmin)

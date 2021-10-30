from django.db import models

# Create your models here.


class Recipe(models.Model):

    class Meta:
        ordering = ['recipe_name']

    # Check this when delete recipe is implemented Docs make me 🤯
    course = models.ForeignKey('Course', on_delete=models.PROTECT)
    recipe_name = models.CharField(max_length=50)
    ingredients = models.TextField(null=True, blank=True)
    steps = models.TextField(null=True, blank=True)
    preparation_time = models.CharField(max_length=5, null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images/')

    def __str__(self):
        return self.recipe_name


class Course(models.Model):

    class Meta:
        verbose_name_plural = 'Courses'

    COURSE_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snacks', 'Snacks'),
        ('desserts', 'Desserts'),
        ('others', 'Others'),
    ]

    course_choice = models.CharField(
        max_length=15,
        choices=COURSE_CHOICES,
    )

    def __str__(self):
        return self.course_choice

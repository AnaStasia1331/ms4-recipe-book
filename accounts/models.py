from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserAccount(models.Model):

    user = models.OneToOneField(User, on_delete=models.PROTECT)
    has_paid = models.BooleanField(default=False)
    token = models.CharField(max_length=50)

    def __str__(self):
        return self.user.username

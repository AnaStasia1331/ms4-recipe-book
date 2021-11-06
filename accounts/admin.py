from django.contrib import admin
from accounts.models import UserAccount


# Register your models here.

class UserAccountAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'has_paid',
    )


admin.site.register(UserAccount, UserAccountAdmin)

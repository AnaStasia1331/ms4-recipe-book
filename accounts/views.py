from django.shortcuts import render

# Create your views here.


def account_settings(request):

    return render(request, 'settings/account_settings.html')

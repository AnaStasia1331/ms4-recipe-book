from django.shortcuts import render

# Create your views here.


def page_not_found_view(request, exception):
    # Source: https://levelup.gitconnected.com/
    # django-customize-404-error-page-72c6b6277317
    return render(request, '404.html', status=404)


def permission_denied_view(request, exception):
    return render(request, '403.html', status=403)

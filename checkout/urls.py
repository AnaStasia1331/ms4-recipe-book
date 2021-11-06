from django.urls import path
from checkout import views

urlpatterns = [
    path('doCheckout', views.checkout, name='checkout'),
    path('success/', views.success, name='success'),
    path('cancel', views.cancel, name='cancel'),
]

from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import auth
import stripe
from django.conf import settings

# Create your views here.


def checkout(request):
    try:
        stripe.api_key = settings.STRIPE_API_KEY
        checkout_session = stripe.checkout.Session.create(
            customer_email=request.user.email,
            submit_type='pay',
            billing_address_collection='auto',
            line_items=[
                {
                    # Provide the exact Price ID (e.g. pr_1234) of the product you want to sell
                    'price': 'price_1JsnjmKjt9KdFmTFVRRJuuVQ',
                    'quantity': 1,
                },
            ],
            payment_method_types=[
              'card',
            ],
            mode='payment',
            success_url=settings.WEBSITE_DOMAIN + reverse('success'),
            cancel_url=settings.WEBSITE_DOMAIN + reverse('cancel'),
        )
    except Exception as e:
        return e.message

    return redirect(checkout_session.url, code=303)


def success(request):
    return render(request, 'checkout/success.html')


def cancel(request):
    return render(request, 'checkout/cancel.html')

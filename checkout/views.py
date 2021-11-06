from django.shortcuts import render, redirect
from django.urls import reverse
import stripe
from django.conf import settings

# Create your views here.


def checkout(request):
    try:
        stripe.api_key = settings.STRIPE_API_KEY
        WEBSITE_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            customer_email='customer@example.com',
            submit_type='donate',
            billing_address_collection='auto',
            shipping_address_collection={
              'allowed_countries': ['US', 'CA'],
            },
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
            success_url=WEBSITE_DOMAIN + reverse('success'),
            cancel_url=WEBSITE_DOMAIN + reverse('cancel'),
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)


def success(request):
    return render(request, 'checkout/success.html')


def cancel(request):
    return render(request, 'checkout/cancel.html')

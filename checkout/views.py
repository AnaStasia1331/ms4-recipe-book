from django.shortcuts import render
from django.urls import reverse
import stripe
from django.conf import settings

# Create your views here.


def checkout(request):
    try:
        stripe.api_key = settings.STRIPE_API_KEY
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
                    'price': 'prod_KXtWCZafaoOBjA',
                    'quantity': 1,
                },
            ],
            payment_method_types=[
              'card',
            ],
            mode='payment',
            success_url=reverse('success'),
            cancel_url=reverse('cancel'),
        )
    except Exception as e:
        return str(e)

    return redirect(checkout_session.url, code=303)

def success(request):
    return render(request, 'checkout/success.html')

def cancel(request):
    return render(request, 'checkout/cancel.html')
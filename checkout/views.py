import uuid
from django.shortcuts import render, redirect
from django.views.decorators.http import require_GET, require_POST
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib import auth
import stripe
from django.conf import settings
from accounts.models import UserAccount

# Create your views here.


@login_required
@require_POST
def checkout(request):
    account = get_or_create_account(request)
    account.token = uuid.uuid4().hex
    account.save()

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
            success_url=settings.WEBSITE_DOMAIN + \
            reverse('success') + '?token=' + account.token,
            cancel_url=settings.WEBSITE_DOMAIN + reverse('cancel'),
        )
    except Exception as e:
        return e.message

    return redirect(checkout_session.url, code=303)


@login_required
@require_GET
def success(request):
    # validate token is correct
    token = request.GET['token']
    if token:
        account = get_or_create_account(request)
        if account.token == token:
            account.has_paid = True
            account.save()
        else:
            return render(request, 'checkout/cancel.html')
    else:
        pass
        # show error page if token doens't exist
    # return success page
    return render(request, 'checkout/success.html')


@login_required
@require_GET
def cancel(request):
    return render(request, 'checkout/cancel.html')


def get_or_create_account(request):
    try:
        account = UserAccount.objects.get(user=request.user)
    except UserAccount.DoesNotExist:
        user = auth.get_user(request)
        account = UserAccount.objects.create(user=user)
    return account

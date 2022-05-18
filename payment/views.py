from rest_framework.decorators import api_view
from rest_framework.response import Response
import os

from .models import Item, Order
from django.conf import settings

DOMAIN = settings.DOMAIN

import stripe
stripe.api_key = settings.STRIPE_SECRET_KEY

from django.http import JsonResponse
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404


class HomePageView(TemplateView):
    template_name = 'payment/home.html'


@api_view(['GET'])
def buy(request, item_id):
    req_item = get_object_or_404(Item, pk=item_id)

    session = stripe.checkout.Session.create(
        line_items=[{
            'name': req_item.name,
            'quantity': 1,
            'currency': req_item.currency,
            'amount': str(req_item.price * 100),
        }],
        mode='payment',
        payment_method_types=['card'],
        success_url=DOMAIN + 'success/',
        cancel_url=DOMAIN + 'cancel/',
        api_key=os.getenv('STRIPE_SECRET_KEY')
    )

    return JsonResponse({'sessionId': session.id})


@api_view(['GET'])
def buy_order(request, order_id):
    req_order = get_object_or_404(Order, id=order_id)

    items = [
        {
            "name": obj.name,
            "quantity": 1,
            "currency": obj.currency,
            "amount": obj.amount,
        } for obj in list(req_order.items)
    ]

    session = stripe.checkout.Session.create(
        line_items=items,
        payment_method_types=['card'],
        mode='payment',
        discounts=[{'coupon': req_order.discount.discount_id}] if req_order.discount else [],
        tax_id_collection={
            'enabled': True,
        },
        success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://example.com/cancel',
    )

    return JsonResponse({'sessionId': session['id']})


@api_view(['GET'])
def stripe_config(request):
    stripe_key = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return Response(stripe_key)


def item(request):
    pass


def order(request):
    pass


class SuccessPageView(TemplateView):
    template_name = 'payment/success.html'


class CancelPageView(TemplateView):
    template_name = 'payment/cancel.html'
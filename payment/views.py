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
from django.views.generic import ListView


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
            'amount': req_item.price * 100,
        }],
        mode='payment',
        payment_method_types=['card'],
        success_url=DOMAIN + 'success/',
        cancel_url=DOMAIN + 'cancel/',
    )

    return Response({'sessionId': session.id})


@api_view(['GET'])
def buy_order(request, order_id):
    req_order = get_object_or_404(Order, id=order_id)

    items = [
        {
            "name": obj.name,
            "quantity": 1,
            "currency": obj.currency,
            "amount": obj.price * 100,
        } for obj in req_order.items.all()
    ]

    session = stripe.checkout.Session.create(
        line_items=items,
        payment_method_types=['card'],
        mode='payment',
        discounts=[{'coupon': req_order.discount.discount_id}] if req_order.discount else [],
        tax_id_collection={
            'enabled': True,
        },
        success_url=DOMAIN + 'success/',
        cancel_url=DOMAIN + 'cancel/',
    )

    return Response({'sessionId': session['id']})


@api_view(['GET'])
def stripe_config(request):
    stripe_key = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
    return Response(stripe_key)


class ItemListView(ListView):

    context_object_name = 'item'
    template_name = 'payment/payment.html'

    def get_queryset(self):
        return Item.objects.get(pk=self.kwargs['item_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'item'
        return context


class OrderListView(ListView):

    context_object_name = 'order'
    template_name = 'payment/payment.html'

    def get_queryset(self):
        return Order.objects.get(pk=self.kwargs['order_id'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['type'] = 'order'
        return context


class SuccessPageView(TemplateView):
    template_name = 'payment/success.html'


class CancelPageView(TemplateView):
    template_name = 'payment/cancel.html'
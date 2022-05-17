from django.shortcuts import render
import stripe

from django.views.generic.base import TemplateView


class HomePageView(TemplateView):
    template_name = 'payment/home.html'


def buy(request):
    session = stripe.checkout.Session.create(
        line_items=[{
            'price': '{{PRICE_ID}}',
            'quantity': 1,
        }],
        mode='payment',
        discounts=[{
            'coupon': '{{COUPON_ID}}',
        }],
        tax_id_collection={
            'enabled': True,
        },
        success_url='https://example.com/success?session_id={CHECKOUT_SESSION_ID}',
        cancel_url='https://example.com/cancel',
    )


def item(request):
    pass


class SuccessPageView(TemplateView):
    template_name = 'payment/success.html'


class CancelPageView(TemplateView):
    template_name = 'payment/cancel.html'
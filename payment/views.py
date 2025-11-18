import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Item
from django.urls import reverse
from django.http import JsonResponse

stripe.api_key = settings.STRIPE_SECRET_KEY


def item(request, pk):
    item = get_object_or_404(Item, pk=pk)
    return render(request, 'payment/item.html',{
        "item": item,
        "STRIPE_PUBLISHABLE_KEY": settings.STRIPE_PUBLISHABLE_KEY,
    })


def buy_item(request, pk):
    item = get_object_or_404(Item, pk=pk)

    success_url = request.build_absolute_uri(reverse('completed'))
    cancel_url = request.build_absolute_uri(reverse('canceled'))

    session_data = {
        'mode':'payment',
        'success_url':success_url,
        'cancel_url': cancel_url,
        'line_items':[{
            'price_data':{
                'currency':'rub',
                'product_data':{
                    'name': item.name,
                },
                "unit_amount": int(item.price * 100)
            },
            'quantity':1
        }]
    }

    session = stripe.checkout.Session.create(**session_data)
    return JsonResponse({"session_id": session.id})

def payment_completed(request):
    return render(request, "payment/completed.html")

def payment_canceled(request):
    return render(request, "payment/canceled.html")

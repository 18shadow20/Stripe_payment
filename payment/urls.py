from django.urls import path
from . import views

urlpatterns = [
    path('buy/<int:pk>/', views.buy_item, name = 'buy_item'),
    path('item/<int:pk>/', views.item, name = "item"),
    path('completed/', views.payment_completed, name = 'completed'),
    path('canceled/', views.payment_canceled, name = 'canceled'),
]
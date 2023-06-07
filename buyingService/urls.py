from django.urls import path

from . import views

urlpatterns = [
    path('transaction/', views.TransactionView.as_view(), name='transaction-create'),
    path('basket/create/', views.BasketCreateView.as_view(), name='basket-create'),
    path('basket/<int:id_basket>/delete/', views.BasketDeleteView.as_view(), name='basket-delete'),
    path('buying/create/', views.BuyingCreateView.as_view(), name='buying-create'),
    path('buying/<int:id_buying>/delete/', views.BuyingDeleteView.as_view(), name='buying-delete'),
]

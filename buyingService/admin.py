from django.contrib import admin
from .models import Transaction, Basket, Buying


class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'transaction_hash')


admin.site.register(Transaction, TransactionAdmin)


class BasketAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'plot')


admin.site.register(Basket, BasketAdmin)


class BuyingAdmin(admin.ModelAdmin):
    list_display = ('id', 'plot', 'date', 'cost', 'buyer', 'owner')


admin.site.register(Buying, BuyingAdmin)

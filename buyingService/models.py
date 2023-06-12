from django.db import models


class Buying(models.Model):
    id = models.AutoField(primary_key=True)
    plot = models.ForeignKey('planetService.Plot', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True, db_index=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    buyer = models.ForeignKey('userService.User', related_name='owner_buying', on_delete=models.CASCADE)
    owner = models.ForeignKey('userService.User', related_name='buyer_buying', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'buying'


class Basket(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey('userService.User', on_delete=models.CASCADE, null=True)
    plot = models.ForeignKey('planetService.Plot', on_delete=models.CASCADE, null=True)

    class Meta:
        db_table = 'basket'


class Transaction(models.Model):
    user = models.ForeignKey('userService.User', on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    transaction_hash = models.CharField(max_length=100)

    class Meta:
        db_table = 'transactions'

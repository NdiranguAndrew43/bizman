"""
libraries to help models work
"""
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class InventoryItem(models.Model):
    """
    a class to handle inventoryitems
    """
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Transaction(models.Model):
    """
    A class to handle Transactions
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link to the User model
    description = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()

    TRANSACTION_TYPES = (
        ('Income', 'Income'),
        ('Expense', 'Expense'),
    )
    type = models.CharField(max_length=7, choices=TRANSACTION_TYPES)

    def __str__(self):
        return f'Transaction {self.id} - {self.amount} by {self.user.username}'

class Events(models.Model):
    """
    a class to handle events
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    event_date = models.DateField()

    def __str__(self):
        return f'Events {self.id} - {self.name} - {self.description} by {self.user.username}'

"""
Importing all needed Django libraries for functionality
"""
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import InventoryItem, Transaction, Events

class UserSignUp(UserCreationForm):
    """
    A class to provide a form for users to register to the app
    """
    email = forms.EmailField()

    class Meta:
        """
        A class to characterise user account information captured
        """
        model = User
        fields = [
            'username', 'email', 'password1', 'password2'
        ]

class InventoryItemForm(forms.ModelForm):
    """
    a form to handle inventory item creation
    """
    class Meta:
        """
        A class to characterise item information
        """
        model = InventoryItem
        fields = ['name', 'quantity']

class TransactionForm(forms.ModelForm):
    """
    a form to handle transaction information collection
    """
    class Meta:
        """
        class to define the information user's will record
        """
        model = Transaction
        fields = ['description', 'amount', 'date', 'type']

class EventForm(forms.ModelForm):
    """
    a form to handle event information collection
    """
    class Meta:
        """
        class to define the information user's will record
        """
        model = Events
        fields = ['name', 'description', 'event_date']

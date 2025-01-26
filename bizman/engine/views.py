"""
Importing all needed Django libraries for functionality
"""
from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import UserSignUp, InventoryItemForm, TransactionForm, EventForm
from .models import InventoryItem, Transaction, Events

class Landing(TemplateView):
    """
    A class to take users to the landing Page
    """
    template_name = 'Landing.html'

class SignUp(View):
    """
    A class to sign up users and create accounts on the page
    """
    def get(self, request):
        """
        function to render the signup form
        """
        form = UserSignUp()
        return render(request, 'SignUp.html', {'form': form})

    def post(self, request):
        """
        function to analyse the signup form,
        posting the form and thus saving the user
        """
        form = UserSignUp(request.POST)

        if form.is_valid():
            form.save()
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1']
            )

            login(request, user)
            return redirect('dashboard')

        return render(request, 'SignUp.html', {'form': form})

class Dashboard(LoginRequiredMixin, View):
    """
    A class for the authenticated user dashboard
    """
    def get(self, request):
        """
        View function to display the dashboard page.
        """

        return render(request, 'Dashboard.html', {'username' : request.user.username})

class InventoryView(LoginRequiredMixin, View):
    """
    a function to render user inventory views
    """
    def get(self, request):
        """
        a function to get the inventory information
        """
        items = InventoryItem.objects.filter(user=self.request.user.id).order_by('name')

        return render(request, 'Inventory.html', {'items': items})

class AddItem(LoginRequiredMixin, CreateView):
    """
    a function to render add inventory item view
    """
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'ItemForm.html'
    success_url = reverse_lazy('inventory')

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['categories'] = Category.objects.all()
    #     return context

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EditItem(LoginRequiredMixin, UpdateView):
    """
    a function to render edit inventory item view
    """
    model = InventoryItem
    form_class = InventoryItemForm
    template_name = 'ItemForm.html'
    success_url = reverse_lazy('inventory')

class DeleteItem(LoginRequiredMixin, DeleteView):
    """
    a function to render delete inventory item view
    """
    model = InventoryItem
    template_name = 'DeleteItem.html'
    success_url = reverse_lazy('inventory')
    context_object_name = 'item'

class TransactionOverview(LoginRequiredMixin, View):
    """
    A class to render a template display for transactions
    """
    def get(self, request):
        """
        a function to get transaction information for display
        """
        transactions = Transaction.objects.filter(user=request.user)
        total_income = sum(t.amount for t in transactions if t.type == 'Income')
        total_expenses = sum(t.amount for t in transactions if t.type == 'Expense')
        net_balance = total_income - total_expenses

        context = {
            'transactions': transactions,
            'total_income': total_income,
            'total_expenses': total_expenses,
            'net_balance': net_balance,
        }

        return render(request, 'TransactionOverview.html', context)

class AddTransaction(LoginRequiredMixin, View):
    """
    A class to define form view for collection of user transaction
    """
    def get(self, request):
        """
        A function to display the form for adding a transaction
        """
        form = TransactionForm()
        return render(request, 'AddEntry.html', {'form': form})

    def post(self, request):
        """
        A function to record transaction information from the user
        """
        form = TransactionForm(request.POST)
        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = request.user
            transaction.save()
            return redirect(reverse('accounting_overview'))
        return render(request, 'AddEntry.html', {'form': form})

class EntryList(LoginRequiredMixin, View):
    """
    A class to render a view for user transactions
    """
    def get(self, request):
        """
        A function to render a view for user transactions
        """
        transactions = Transaction.objects.filter(user=request.user)
        return render(request, 'EntryList.html', {'transactions': transactions})

class EditEntry(LoginRequiredMixin, UpdateView):
    """
    A class to render a view for user's to edit transactions
    """
    model = Transaction
    form_class = TransactionForm
    template_name = 'EditEntry.html'
    success_url = reverse_lazy('entry_list')
    pk_url_kwarg = 'entry_id'  # This line is vital if using entry_id

# class DeleteEntry(LoginRequiredMixin, View):
#     """
#     A class to render a view for user's to edit transactions
#     """
#     def delete_entry(self, request, entry_id):
#         """
#         A function to allow users delete transactions
#         """
#         transaction = get_object_or_404(Transaction, id=entry_id, user=request.user)

#         if request.method == 'POST':
#             transaction.delete()
#             return redirect('EntryList')

#         return render(request, 'DeleteEntry.html', {'transaction': transaction})

class DeleteEntry(LoginRequiredMixin, DeleteView):
    """
    a function to render delete transac view
    """
    model = Transaction
    template_name = 'DeleteEntry.html'
    success_url = reverse_lazy('entry_list')
    pk_url_kwarg = 'entry_id'

class EventList(LoginRequiredMixin, View):
    """
    A class to render a template display for transactions
    """
    def get(self, request):
        """
        A function to get transaction information for the logged-in user
        """
        events = Events.objects.filter(user=request.user)

        context = {
            'events': events,  # Pass the fetched events to the context
        }

        return render(request, 'EventList.html', context)


class AddEvent(LoginRequiredMixin, View):
    """
    A class to define form view for collection of user transaction
    """
    def get(self, request):
        """
        A function to display the form for adding a transaction
        """
        form = EventForm()
        return render(request, 'AddEvent.html', {'form': form})

    def post(self, request):
        """
        A function to record transaction information from the user
        """
        form = EventForm(request.POST)
        if form.is_valid():
            Events = form.save(commit=False)
            Events.user = request.user
            Events.save()
            return redirect(reverse('event_list'))
        return render(request, 'AddEvent.html', {'form': form})


class EditEvent(LoginRequiredMixin, UpdateView):
    """
    A class to render the edit event view
    """
    model = Events
    form_class = EventForm
    template_name = 'EditEvent.html'
    success_url = reverse_lazy('event_list')
    pk_url_kwarg = 'event_id'

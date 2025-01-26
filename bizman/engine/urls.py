"""
Importing all needed Django libraries for functionality
"""
from django.urls import path
from django.contrib.auth import views as auth_views
from .views import (
    Landing,
    SignUp,
    Dashboard,
    InventoryView,
    DeleteItem,
    AddItem,
    EditItem,
    TransactionOverview,
    AddTransaction,
    EntryList,
    EditEntry,
    DeleteEntry,
    EventList,
    AddEvent,
    EditEvent,
)

urlpatterns = [
    path('', Landing.as_view(), name='landing'),
    path('signup/', SignUp.as_view(), name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='Login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Logout.html'), name='logout'),
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('inventory/', InventoryView.as_view(), name='inventory'),
    path('add-item/', AddItem.as_view(), name='add-item'),
    path('edit-item/<int:pk>', EditItem.as_view(), name='edit-item'),
    path('delete-item/<int:pk>', DeleteItem.as_view(), name='delete-item'),
    path('transactions/', TransactionOverview.as_view(), name='accounting_overview'),
    path('add/', AddTransaction.as_view(), name='add_entry'),
    path('entries/', EntryList.as_view(), name='entry_list'),
    path('edit/<int:entry_id>/', EditEntry.as_view(), name='edit_entry'),
    path('delete/<int:entry_id>/', DeleteEntry.as_view(), name='delete_entry'),
    path('events/', EventList.as_view(), name='event_list'),
    path('addevent/', AddEvent.as_view(), name='add_event'),
    path('editevent/<int:event_id>/', EditEvent.as_view(), name='edit_event')
]

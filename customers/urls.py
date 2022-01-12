from django.urls import path, include

from customers.views import CustomerListView

app_name = 'customer'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer'),
]

from django.urls import path, include

from customers.views import CustomerListView, CustomerDetailView

app_name = 'customer'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer'),
    path('detail/<int:customer_id>/', CustomerDetailView.as_view(), name='customer_info'),
]

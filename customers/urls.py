from django.urls import path, include

from customers.views import CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, \
    CustomerDeleteView

app_name = 'customer'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer'),
    path('detail/<int:customer_id>/', CustomerDetailView.as_view(), name='customer_info'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
]

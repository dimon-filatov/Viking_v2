from django.urls import path, include

from customers.views import CustomerListView, CustomerDetailView, CustomerCreateView, CustomerUpdateView, \
    CustomerDeleteView, CustomerFullListView, CustomerFullCreateView, CustomerFullUpdateView, CustomerFullDeleteView

app_name = 'customer'

urlpatterns = [
    path('', CustomerListView.as_view(), name='customer'),
    path('detail/<int:customer_id>/', CustomerDetailView.as_view(), name='customer_info'),
    path('create/', CustomerCreateView.as_view(), name='customer_create'),
    path('update/<int:pk>/', CustomerUpdateView.as_view(), name='customer_update'),
    path('delete/<int:pk>/', CustomerDeleteView.as_view(), name='customer_delete'),
    path('customer_full_details/<customer_for_full>/', CustomerFullListView.as_view(), name='customer_full'),
    path('customer_full/create/<int:pk>/', CustomerFullCreateView.as_view(), name='customer_full_create'),
    path('customer_full/update/<int:pk>/', CustomerFullUpdateView.as_view(), name='customer_full_update'),
    path('customer_full/delete/<int:pk>/', CustomerFullDeleteView.as_view(), name='customer_full_delete'),
]

from django.urls import path, include

from deliveries.views import DeliveryAddressListView, DeliveryAddressCreateView, DeliveryAddressUpdateView, \
    DeliveryAddressDeleteView

app_name = 'delivery'

urlpatterns = [
    path('address_lst/<customer_for_delivery>/', DeliveryAddressListView.as_view(), name='customer_delivery_address'),
    path('address/create/<int:pk>/', DeliveryAddressCreateView.as_view(), name='customer_delivery_address_create'),
    path('address/update/<int:pk>/', DeliveryAddressUpdateView.as_view(), name='customer_delivery_address_update'),
    path('address/delete/<int:pk>/', DeliveryAddressDeleteView.as_view(), name='customer_delivery_address_delete'),
]

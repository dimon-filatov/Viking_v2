from django.urls import path

from productions.views import ProductionsListView, ProductionsCreateView, ProductionsDetailView, ProductionsUpdateView, \
    ProductionsDeleteView

app_name = 'product'

urlpatterns = [
    path('read_all/', ProductionsListView.as_view(), name='products'),
    path('create/', ProductionsCreateView.as_view(), name='product_create'),
    path('product_info/<int:product_id>/', ProductionsDetailView.as_view(), name='product_info'),
    path('update_stage/<int:pk>/', ProductionsUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductionsDeleteView.as_view(), name='products_delete'),
]

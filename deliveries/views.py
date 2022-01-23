from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from customers.models import Customer
from deliveries.forms import DeliveryAddressEditForm
from deliveries.models import DeliveryAddress


class DeliveryAddressListView(ListView):
    model = DeliveryAddress
    template_name = "deliveries/delivery_address.html"
    context_object_name = 'customers_address_for_delivery_lst'
    fields = '__all__'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeliveryAddressListView, self).get_context_data()
        context['title'] = 'Адреса доставки'
        context['pk_of_customer'] = self.kwargs.get('customer_for_delivery', None)
        context['company_name'] = get_object_or_404(Customer, pk=context['pk_of_customer']).name

        return context

    def get_queryset(self):
        customer_for_delivery = self.kwargs.get('customer_for_delivery', None)
        if customer_for_delivery is not None:
            customer = get_object_or_404(Customer, pk=customer_for_delivery)
            object_list = DeliveryAddress.objects.filter(customer=customer)
            return object_list
        else:
            return reverse('customer:customer')


class DeliveryAddressCreateView(CreateView):
    model = DeliveryAddress
    template_name = 'deliveries/delivery_address_update.html'
    form_class = DeliveryAddressEditForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeliveryAddressCreateView, self).get_context_data()
        context['title'] = 'Адрес/создание'
        return context

    def get_success_url(self):
        return reverse('delivery:customer_delivery_address', kwargs={'customer_for_delivery': self.object.customer.id})

    def get_initial(self):
        initial = super().get_initial()
        initial['customer'] = get_object_or_404(Customer, pk=self.kwargs['pk'])
        return initial


class DeliveryAddressUpdateView(UpdateView):
    model = DeliveryAddress
    template_name = 'deliveries/delivery_address_update.html'
    form_class = DeliveryAddressEditForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeliveryAddressUpdateView, self).get_context_data()
        context['title'] = 'Адресс/редактировать'

        return context

    def get_success_url(self):
        return reverse('delivery:customer_delivery_address', kwargs={'customer_for_delivery': self.object.customer.id})


class DeliveryAddressDeleteView(DeleteView):
    model = DeliveryAddress
    template_name = 'deliveries/delivery_address_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(DeliveryAddressDeleteView, self).get_context_data()
        context['title'] = 'Адрес/удаление'

        return context

    def get_success_url(self):
        return reverse('delivery:customer_delivery_address', kwargs={'customer_for_delivery': self.object.customer.id})

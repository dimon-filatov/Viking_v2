from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from customers.forms import CustomerEditForm, CustomerFullEditForm
from customers.models import Customer, CustomerFull
from productions.models import Production


class CustomerListView(ListView):
    model = Customer
    template_name = "customers/customer.html"
    context_object_name = 'objects'
    fields = '__all__'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerListView, self).get_context_data()
        context['title'] = 'Все клиенты'

        return context


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/one_customer.html'
    pk_url_kwarg = 'customer_id'
    context_object_name = 'customer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerDetailView, self).get_context_data()
        context['title'] = self.object

        return context


class CustomerCreateView(CreateView):
    model = Customer
    template_name = 'customers/customer_update.html'
    form_class = CustomerEditForm
    success_url = reverse_lazy('customer:customer')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerCreateView, self).get_context_data()
        context['title'] = 'Клиент/создание'
        return context


class CustomerUpdateView(UpdateView):
    model = Customer
    template_name = 'customers/customer_update.html'
    form_class = CustomerEditForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerUpdateView, self).get_context_data()
        context['title'] = 'Клиенты/редактировать'

        return context

    def get_success_url(self):
        return reverse('customer:customer_info', kwargs={'customer_id': self.kwargs['pk']})


class CustomerDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_delete.html'
    success_url = reverse_lazy('customer:customer')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerDeleteView, self).get_context_data()
        context['title'] = 'продукт/удаление'

        return context


class CustomerFullListView(ListView):
    model = CustomerFull
    template_name = "customers/customers_full.html"
    context_object_name = 'customers_full_lst'
    fields = '__all__'
    paginate_by = 50

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerFullListView, self).get_context_data()
        context['title'] = 'юр. лица'

        return context


class CustomerFullCreateView(CreateView):
    model = CustomerFull
    template_name = 'customers/customer_update.html'
    form_class = CustomerFullEditForm
    success_url = reverse_lazy('customer:customer_full')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerFullCreateView, self).get_context_data()
        context['title'] = 'Клиент/создание'
        return context


class CustomerFullUpdateView(UpdateView):
    model = CustomerFull
    template_name = 'customers/customer_update.html'
    form_class = CustomerFullEditForm
    success_url = reverse_lazy('customer:customer_full')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerFullUpdateView, self).get_context_data()
        context['title'] = 'Клиенты/редактировать'

        return context


class CustomerFullDeleteView(DeleteView):
    model = Customer
    template_name = 'customers/customer_full_delete.html'
    success_url = reverse_lazy('customer:customer')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerFullDeleteView, self).get_context_data()
        context['title'] = 'продукт/удаление'

        return context

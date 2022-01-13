from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from customers.forms import CustomerEditForm
from customers.models import Customer
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
    template_name = 'customers/customer_create.html'
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
    success_url = reverse_lazy('customer:customer')

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

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_deleted = True
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())

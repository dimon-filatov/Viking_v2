from django.db.models import Q
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
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

        if self.request.GET.get('q'):
            context['search'] = f'Поиск по значению: {self.request.GET.get("q")}'
        else:
            context['search'] = 'Все клиенты'

        return context

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = Customer.objects.filter(
                Q(name__icontains=query.lower()) |
                Q(full_name__full_name__icontains=query.lower()),
            )
            return object_list
        else:
            return Customer.objects.all()


class CustomerDetailView(DetailView):
    model = Customer
    template_name = 'customers/one_customer.html'
    pk_url_kwarg = 'customer_id'
    context_object_name = 'customer'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerDetailView, self).get_context_data()
        context['title'] = self.object
        context['full_name_lst'] = context['object'].full_name.filter(is_deleted=False)
        context['delivery_address_lst'] = context['object'].delivery_address.filter(is_deleted=False)

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
        context['pk_of_customer'] = self.kwargs.get('customer_for_full', None)
        context['company_name'] = get_object_or_404(Customer, pk=context['pk_of_customer']).name

        return context

    def get_queryset(self):
        customer_for_full = self.kwargs.get('customer_for_full', None)
        if customer_for_full is not None:
            customer = get_object_or_404(Customer, pk=customer_for_full)
            object_list = CustomerFull.objects.filter(customer=customer)
            return object_list
        else:
            return reverse('customer:customer')


class CustomerFullCreateView(CreateView):
    model = CustomerFull
    template_name = 'customers/customer_update.html'
    form_class = CustomerFullEditForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerFullCreateView, self).get_context_data()
        context['title'] = 'Клиент/создание'
        return context

    def get_success_url(self):
        return reverse('customer:customer_full', kwargs={'customer_for_full': self.object.customer.id})

    def get_initial(self):
        initial = super().get_initial()
        initial['customer'] = get_object_or_404(Customer, pk=self.kwargs['pk'])
        return initial


class CustomerFullUpdateView(UpdateView):
    model = CustomerFull
    template_name = 'customers/customer_update.html'
    form_class = CustomerFullEditForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerFullUpdateView, self).get_context_data()
        context['title'] = 'Клиенты/редактировать'

        return context

    def get_success_url(self):
        return reverse('customer:customer_full', kwargs={'customer_for_full': self.object.customer.id})


class CustomerFullDeleteView(DeleteView):
    model = CustomerFull
    template_name = 'customers/customer_full_delete.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(CustomerFullDeleteView, self).get_context_data()
        context['title'] = 'продукт/удаление'

        return context

    def get_success_url(self):
        return reverse('customer:customer_full', kwargs={'customer_for_full': self.object.customer.id})

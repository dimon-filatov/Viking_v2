from django.views.generic import ListView, DetailView

from customers.models import Customer


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

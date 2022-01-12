from django.views.generic import ListView

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

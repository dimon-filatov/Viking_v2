from django.http import HttpResponseRedirect, request
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView

from productions.forms import ProductCreateForm
from productions.models import Production, ProductStage, ProductStageOptions


class ProductionsListView(ListView):
    model = Production
    template_name = "productios/products.html"
    context_object_name = 'objects'
    fields = '__all__'
    paginate_by = 50

    def get_queryset(self):
        return Production.objects.order_by('is_deleted', 'our_number')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductionsListView, self).get_context_data()
        context['title'] = 'Все штампы'

        return context


class ProductionsCreateView(CreateView):
    model = Production
    template_name = 'productios/product_create.html'
    form_class = ProductCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductionsCreateView, self).get_context_data()
        context['title'] = 'Штамп/создание'
        return context

    def form_valid(self, form):
        self.object = form.save()
        ProductStage.objects.create(production=self.object, product_stage=ProductStageOptions.objects.get(id=2))
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('product:product_info', kwargs={'product_id': self.object.pk})


class ProductionsDetailView(DetailView):
    model = Production
    template_name = 'productios/product_info.html'
    pk_url_kwarg = 'product_id'
    context_object_name = 'product'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductionsDetailView, self).get_context_data()
        context['title'] = self.object

        return context


class ProductionsUpdateView(UpdateView):
    model = Production
    template_name = 'productios/product_create.html'
    success_url = reverse_lazy('product:products')
    form_class = ProductCreateForm

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductionsUpdateView, self).get_context_data()
        context['title'] = 'Штампы/Изменение статуса'

        return context

    def get_success_url(self):
        return reverse('product:product_info', kwargs={'product_id': self.kwargs['pk']})


class ProductionsDeleteView(DeleteView):
    model = Production
    template_name = 'productios/product_delete.html'
    success_url = reverse_lazy('product:products')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ProductionsDeleteView, self).get_context_data()
        context['title'] = 'штамп/удаление'

        return context

    def form_valid(self, form):
        self.object.comment_for_deleted = form.data['comment']
        self.object.save()
        self.object.delete()
        return HttpResponseRedirect(self.get_success_url())
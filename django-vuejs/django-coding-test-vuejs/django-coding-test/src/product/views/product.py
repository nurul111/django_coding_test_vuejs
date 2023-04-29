from django.views import generic

from product.models import Variant

from django.views.generic import ListView, CreateView, UpdateView,TemplateView

from product.forms import VariantForm
#from product.models import Variant


class CreateProductView(generic.TemplateView):
    form_class = VariantForm
    model = Variant
    template_name = 'products/create.html'
    success_url = '/product/products'


class ProductView(CreateProductView, ListView):
    template_name = 'products/list.html'
    paginate_by = 10

    def get_queryset(self):
        filter_string = {}
        print(self.request.GET)
        for key in self.request.GET:
            if self.request.GET.get(key):
                filter_string[key] = self.request.GET.get(key)
        return Variant.objects.filter(**filter_string)

#class CreateProductView(generic.TemplateView):
    #template_name = 'products/create.html'

    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        context['product'] = True
        context['variants'] = list(variants.all())
        return context
class ProductCreateView(CreateProductView, CreateView):
    pass


class ProductEditView(CreateProductView, UpdateView):
    pk_url_kwarg = 'id'
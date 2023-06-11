from django.shortcuts import render, get_object_or_404
from main.forms import Product2CartFrom
from main.models import Product
from cart.cart import Cart
from django.views.generic import ListView

def product_details(request, product_id):
    prod = get_object_or_404(Product, pk=product_id)
    cart = Cart(request)

    if request.method == "POST":
        form = Product2CartFrom(request.POST)
        if form.is_valid():
            cart[str(product_id)] = form.cleaned_data['count']
            count = form.cleaned_data['count']
            cart[product_id] = count
            form = Product2CartFrom()

    else:
        form = Product2CartFrom()

    if str(product_id) in cart.session['cart'].keys():
        in_cart = f'Добавлено в карзину {cart[str(product_id)]} шт'
    else:
        in_cart = None

    context = {'product': prod,
               'form': form,
               'in_cart': in_cart}
    return render(request, 'main/product_details.html', context)

def product_list(request):
    product_list = Product.objects.all()
    return render(request, 'main/product_list.html', {'title': 'Главная страница', 'tovar_list':product_list })

class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'tovar_list'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        from django.core.paginator import Paginator
        paginator = Paginator(self.object_list, self.paginate_by)
        try:
            page = self.request.GET.get('page')
        except:
            page = 1

        try:
            context[self.context_object_name] = paginator.page(page)
        except:
            context[self.context_object_name] = paginator.page(1)


        context['object_count'] = self.model.objects.count()
        context['paginator'] = paginator
        return context


class ProductList2View(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'tovar_list'
    paginate_by = 4

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        from django.core.paginator import Paginator
        paginator = Paginator(self.object_list, self.paginate_by)
        try:
            page = self.request.GET.get('page')
        except:
            page = 1

        try:
            context[self.context_object_name] = paginator.page(page)
        except:
            context[self.context_object_name] = paginator.page(1)


        context['object_count'] = self.model.objects.count()
        context['paginator'] = paginator
        return context



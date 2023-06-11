from django.shortcuts import render
from django.views.generic import ListView
from cart.cart import Cart
from main.models import Product
from django.http import JsonResponse
from django.core.exceptions import PermissionDenied

class CartListView(ListView):
    model = Product
    template_name = 'cart/cart.html'
    context_object_name = 'products'
    #extra_context = 'products'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cart = Cart(self.request)
        ids = list(map(int, list(cart.keys())))
        products = Product.objects.filter(id__in=ids)
        context['products'] = products
        context['cart'] = self.request.session['cart']
        return context

def change_product_view(request, pk, count):
    cart = Cart(request)
    cart[str(pk)] = str(count)
    return JsonResponse({})

def delete_from_cart(request, pk):
    if not request.is_ajax():
        raise PermissionDenied()
    cart = Cart(request)
    try:
        del cart[str(pk)]
    except KeyError as e:
        return JsonResponse({'successed': False})
    return JsonResponse({'successed': True})






from django.urls import path
from . import views
from .views import CartListView, delete_from_cart, change_product_view

app_name = 'cart'

urlpatterns = [
    path('', CartListView.as_view(), name='cart'),
    path('delete/<int:pk>/', delete_from_cart, name='delete'),
    path('change/<int:pk>/<int:count>/', change_product_view, name='change')
]

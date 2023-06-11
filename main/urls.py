from django.urls import path, include
from . import views
from .views import ProductListView, ProductList2View

app_name = 'main'

urlpatterns = [
    path('', ProductListView.as_view(), name='list'),
    path('product_details/<int:product_id>/', views.product_details, name='details'),
    path('ajax_list/', ProductList2View.as_view(), name='ajax_list')
]

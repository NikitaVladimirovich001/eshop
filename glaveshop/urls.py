from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls', namespace='products')),
    path('cart/', include('cart.urls', namespace='cart')),
    path('auth/', include('auth.urls', namespace='auth')),
]

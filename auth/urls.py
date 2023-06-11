from django.urls import path, include
from . import views
from django.urls import path
from auth.views import RegisterView

app_name = 'custom_auth'

urlpatterns = [
    path('sing-up/', RegisterView.as_view(), name='register'),
]

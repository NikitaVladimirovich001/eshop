from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView

from auth.forms import CustomUserRegister
from auth.models import CustomUser
from glaveshop import settings


class RegisterView(CreateView):
    model = CustomUser
    form_class = CustomUserRegister
    template_name = 'auth/register.html'
    success_url = reverse_lazy('product:list')

    def post(self, request, *args, **kwargs):

        if self.form_class(request.POST).is_valid():
            message = render(request, 'auth/vefiry_register.html')
            send_mail(subject="Регистрация на сайте",
                      message='Для подтверждения перейдите по ссылке',
                      from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[request.POST.get('email')])
        result = super().post(request, *args, **kwargs)
        return result

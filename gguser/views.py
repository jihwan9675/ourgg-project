from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm
from .models import User

class LoginView(FormView): # http://ip:port/login
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        # if request is valid, then Server set session key.
        self.request.session['user'] = form.data.get('userid')
        return super().form_valid(form)


class RegisterView(FormView): # http://ip:port/register
    template_name = 'register.html'
    form_class = RegisterForm
    success_url = '/login/'

    def form_valid(self, form):
        # Create User column(Regist)
        user = User(
            userid=form.data.get('userid'),
            username=form.data.get('username'),
            password=make_password(form.data.get('password')),
        )
        user.save()

        return super().form_valid(form)

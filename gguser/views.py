from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.contrib.auth.hashers import make_password
from .forms import RegisterForm, LoginForm, IndexForm
from .models import User
from summoner.forms import SummonerForm


def logout(request):  # http://ip:port/logout
    del(request.session['user'])
    return redirect('/')


class IndexView(FormView):
    template_name = 'index.html'
    form_class = IndexForm
    success_url = '/'

    def get(self, request, *args, **kwargs):  # GET Method (preidct/)
        form = self.form_class(request, initial=self.initial)

        return render(request, self.template_name, {'form': form, 'username': request.session.get('user')})

    def post(self, request, *args, **kwargs):
        print(request.POST['userName'])
        #return render(request, 'summoner.html', {'username': request.session.get('user')})
        #return redirect('/summoner/'+request.POST['userName'], {'username': request.session.get('user')})   
        return redirect('/summoner/?api=123', {'username': request.session.get('user')})   

    def get_form_kwargs(self, **kwargs):
        kw = super().get_form_kwargs(**kwargs)
        kw.update({
            'request': self.request
        })

        return kw


class LoginView(FormView):  # http://ip:port/login
    template_name = 'login.html'
    form_class = LoginForm
    success_url = '/'

    def form_valid(self, form):
        # if request is valid, then Server set session key.
        self.request.session['user'] = form.data.get('userid')

        return super().form_valid(form)


class RegisterView(FormView):  # http://ip:port/register
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

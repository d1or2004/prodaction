from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.views.generic import CreateView

from product.models import Product
from .forms import RegistrationForm, LoginForm
from .models import Contact


class LandingPage(View):

    def get(self, request):
        search = request.GET.get('search')
        if not search:
            products = Product.objects.all()
            context = {'products': products}
            return render(request, 'main/index.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {'products': products}
                return render(request, 'main/index.html', context)
            else:
                context = {'products': products}
                return render(request, 'main/index.html', context)


class SignUpPageView(CreateView):
    form_class = RegistrationForm
    model = User
    success_url = 'login/'
    template_name = 'main/sign.html'


class LoginPageView(View):

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, 'main/login.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        username = form['username'].value()
        password = form['password'].value()
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('landing')

        return render(request, 'main/login.html', {'form': form})


class LogoutPageView(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        return redirect('landing')


class Register(TemplateView):
    template_name = 'main/user.html'


class ContactPageView(View):
    def get(self, request):
        contacts = Contact.objects.all()
        context = {'contacts': contacts}
        return render(request, 'main/contact.html', context)

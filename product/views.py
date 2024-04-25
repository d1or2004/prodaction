from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from .models import ShopDetails, Product
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required


class ProductListView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            products = Product.objects.all()
            context = {'products': products}
            print(products)
            return render(request, 'main/index.html', context)
        else:
            products = Product.objects.filter(name__icontains=search)
            if products:
                context = {'products': products}
                print("________________________________")
                print(products)
                return render(request, 'main/index.html', context)
            else:
                context = {'products': products}
                return render(request, 'main/index.html', context)


class ShopView(View):
    def get(self, request):
        shop = ShopDetails.objects.all()
        context = {'shop': shop}
        return render(request, 'main/shop.html', context)


class HomeView(View):
    def get(self, request):
        home = Product.objects.all()
        context = {'home': home}
        return render(request, 'main/index.html', context)


class Savat(LoginRequiredMixin, View):
    login_url = 'login/'

    def get(self, request, id):
        product = Product.objects.get(id=id)
        context = {'product': product}
        return render(request, 'main/savat.html', context)


@login_required(login_url='login/')
def savat(request):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        context = {'product': product}
        return render(request, 'main/savat.html', context)


class CategoryView(View):
    def get(self, request, id):
        category = Product.objects.get(id=id)
        context = {'category': category}
        return render(request, 'main/index.html', context)


class ProductUpdateView(View):
    def get(self, request, id):
        products = Product.objects.filter(category_id=id)
        context = {'products': products}
        return render(request, 'main/index.html', context)


class CartView(View):
    def get(self, request):
        cards = Product.objects.all()
        context = {'cards': cards}
        return render(request, 'main/cart.html', context)


class Chakcaut(View):
    def get(self, request):
        chakcaut = Product.objects.all()
        context = {'chakcaut': chakcaut}
        return render(request, 'main/chackout.html', context)


class Testimonial(View):
    def get(self, request):
        testimonial = Product.objects.all()
        context = {'testimonial': testimonial}
        return render(request, 'main/testimonial.html', context)


class PageView(View):
    def get(self, request):
        page = Product.objects.all()
        context = {'page': page}
        return render(request, 'main/404.html', context)

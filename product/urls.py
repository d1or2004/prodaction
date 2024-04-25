from django.urls import path
from .views import ProductListView, ShopView, HomeView, Savat, ProductUpdateView, CategoryView, savat, CartView, Chakcaut, Testimonial,PageView
urlpatterns = [
    path('detail/', ProductListView.as_view(), name='product-list'),
    path('shop/', ShopView.as_view(), name='product-shop'),
    # path('savat/<int:id>', Savat.as_view(), name='product-savat'),
    path('savat/<int:id>', savat, name='product-savat'),
    path('category/<int:id>', CategoryView.as_view(), name='category'),
    path('pd/<int:id>', ProductUpdateView.as_view(), name='pd'),
    path('cart/', CartView.as_view(), name='card'),
    path('chakcaut/', Chakcaut.as_view(), name='chakcaut-page'),
    path('testimonial/', Testimonial.as_view(), name='testi'),
    path('page/', PageView.as_view(), name='page'),

]
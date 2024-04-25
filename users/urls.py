from django.urls import path
from .views import SignUpPageView, LoginPageView, LandingPage, LogoutPageView, Register, ContactPageView

urlpatterns = [
    path('', LandingPage.as_view(), name='landing'),
    path('sign/', SignUpPageView.as_view(), name='sign'),
    path('login/', LoginPageView.as_view(), name='login'),
    path('logout/', LogoutPageView.as_view(), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]

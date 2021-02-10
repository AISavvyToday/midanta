"""midanta URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from products.views import HomeView, CategoryView, BlogView, ContactUsView
from accounts.views import RegisterView, LogInView, LogOutView
from carts.views import CartView
from orders.views import TrackOrderView

urlpatterns = [
    # products urls
    path('admin/', admin.site.urls),
    path('', HomeView, name='home'),
    path('category/', CategoryView, name='category'),
    path('blog/', BlogView, name='blog'),
    path('contact/', ContactUsView, name='contact'),

    # user urls
    path('register/', RegisterView, name='register'),
    path('login/', LogInView, name='login'),
    path('logout/', LogOutView, name='logout'),

    # path('accounts/', include('django.contrib.auth.urls')),

    # carts urls
    path('cart/', CartView, name='cart'),

    # order urls
    path('track-order/', TrackOrderView, name='track-order'),
]

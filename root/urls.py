"""root URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from account.views import (
    index_view,
    signin_view,
    signup_view,
    auth_view,
    test_view,
    resend_otp,
    test2_view
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', index_view, name='home'),
    path('home/signin/', signin_view, name='signin'),
    path('home/signup/', signup_view, name='signup'),
    path('home/auth/<username>/', auth_view, name='auth'),
    path('home/auth/', auth_view, name='auth2'),
    path('test/', test_view, name='test'),
    path('resend/<username>', resend_otp, name='resend'),
    path('test2/', test2_view, name='test2'),
]

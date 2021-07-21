"""shoppingproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from user import views as A
from product import views as B

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',B.home, name="home"),
    # user
    path('user/signup', A.user_signup, name="signup"),
    path('user/login', A.user_login, name="login"),
    path('user/logout', A.user_logout, name="logout"),
    path('user/mypage', A.mypage, name="mypage"),

    # product
    path('product/<str:id>', B.detail, name="detail"),
    path('product/post/', B.make_post, name="post"),
    path('product/update/<str:id>', B.edit, name="edit"),
    path('product/delete/<str:id>', B.delete, name="delete"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


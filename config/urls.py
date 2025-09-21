"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
<<<<<<< HEAD
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
=======
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
>>>>>>> bb8d60eaff9c79db86becab91c8e18145f023ed4
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
<<<<<<< HEAD
from django.urls import path,include
from django.views.generic.base import TemplateView
urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/',include('accounts.urls')),
    path('accounts/',include('django.contrib.auth.urls')),
    path("", TemplateView.as_view(template_name="home.html"),name="home"), # new

    # path('pages/',include('pages.urls')),
=======
from django.urls import path

urlpatterns = [
    path("admin/", admin.site.urls),
>>>>>>> bb8d60eaff9c79db86becab91c8e18145f023ed4
]

"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.contrib import admin # type: ignore
from django.urls import path # type: ignore
from portfolio import views
from portfolio.views import *
from django.conf.urls.i18n import i18n_patterns # type: ignore
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",home_view,name="home"),
    path("show",show_view,name="show"),    
    path('download/<int:pk>/', views.download_pdf, name='download_pdf'),
    path("contact", views.contact_show, name="contact")
]

urlpatterns = [
    *i18n_patterns(*urlpatterns, prefix_default_language=False),
    path("set-language/<str:language>", views.set_language, name="set-language"),
]
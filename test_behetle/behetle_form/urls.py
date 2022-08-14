"""behetle_form URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path
from django.contrib import admin
#from django.urls import re_path
#from behetle import views
from django.views.generic import TemplateView

from behetle import views
from django.urls import path, include

"""
urlpatterns = [
    path('', views.index, name='home'),
    re_path(r'^about', views.about),
    re_path(r'^contact', views.contact),
]
"""
"""
urlpatterns = [
    #path('products/', views.products),
    path('products/<int:productid>/', views.products),
    #path('product/', views.users),
    path('users/', views.users),
]
"""
"""
urlpatterns = [
    path('', views.index),
    path('about/', views.about),
    path('contact/', views.contact),
    path('details/', views.details),
]
"""
"""
urlpatterns = [
    path('', TemplateView.as_view(template_name="behetle/index.html")),
    path('about/', TemplateView.as_view(template_name="behetle/about.html", 
        extra_context={"header": "О сайте"})), 
    path('contact/', TemplateView.as_view(template_name="behetle/contact.html")),
]
"""
app_name = "behetle"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
]


"""
path('', views.index),
path('create/', views.create),
path('edit/<int:id>', views.edit),
path('delete/<int:id>/', views.delete),
"""
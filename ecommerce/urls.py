"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.conf.urls import url, include
from home.views import index, contacts
from accounts import urls as urls_accounts 
from products import urls as urls_products  
from cart import urls as urls_cart 
from checkout import urls as urls_checkout 
from brands import urls as urls_brands
from search import urls as urls_search
from products.views import all_products 
from django.views import static 
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),  
    url(r'^$', index, name='home'),
    url(r'^contacts/',contacts, name='contacts'),
    url(r'^accounts/', include(urls_accounts)), 
    url(r'^search/', include(urls_search)), 
    url(r'^checkout/',include(urls_checkout)),
    url(r'^products/', include(urls_products)),  
    url(r'^brands/', include(urls_brands)), 
    url(r'^media/(?P<path>.*)$',static.serve,{'document_root': settings.MEDIA_ROOT}), 
    url(r'^cart/',include(urls_cart)),
]


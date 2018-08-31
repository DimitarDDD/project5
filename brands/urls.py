from django.conf.urls import url, include 
from .views import all_brands
urlpatterns = [ 
    url(r'^$', all_brands, name= "brands"),
    ]
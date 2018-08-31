from django.conf.urls import url 
from home.views import index, contacts

urlpatterns = [ 
    url(r'^$',home, name='home'), 
    url(r'^contacts/',contacts, name='contacts')
    ]
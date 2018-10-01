from django.conf.urls import url, include
from .views import add_a_review,  edit_a_review, delete_review

urlpatterns = [
    url(r'(?P<pk>\d+)/add$', add_a_review, name='add_a_review'),
  
    url(r'^(?P<pk>\d+)/edit_a_review$', edit_a_review, name='edit_a_review'), 
    url(r'^/delete-review$', delete_review, name='delete_review'),
]
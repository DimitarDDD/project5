from django.conf.urls import url, include
from .views import add_a_review, review_content, edit_a_review, delete_review

urlpatterns = [
    url(r'^add/$', add_a_review, name='add_a_review'),
    url(r'^(?P<pk>\d+)$', review_content, name='review_content'),
    url(r'^(?P<pk>\d+)/edit_a_review$', edit_a_review, name='edit_a_review'), 
    url(r'^(?P<pk>\d+)/delete-review$', delete_review, name='delete_review'),
]
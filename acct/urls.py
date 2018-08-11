from django.conf.urls import url
from acct import views


urlpatterns = [
    url('r^$', views.index, name='index'),
    url(r'^request_form/', views.request_form, name='request_form'),
]

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^list$', views.address_list, name='address_list'),
    url(r'^add$', views.address_new, name='address_new'),

]
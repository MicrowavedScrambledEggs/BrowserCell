'''
Created on 5/10/2017

@author: Admin
'''

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
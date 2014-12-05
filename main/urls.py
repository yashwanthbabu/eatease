from django.contrib import admin
from django.conf.urls import patterns, url
from . import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^search/$', views.search, name='search'),
	url(r'^search/(?P<place_url>[-!\w]+)$', views.search, name='search'),
	url(r'^search_list/$', views.search_list, name='search_list'),
	url(r'^restaurant/(?P<rest_url>[-!\w]+)/$', views.restaurant, name='restaurant'),
	url(r'^filter_test/$', views.filter_test, name='filter_test'),
)
from django.contrib import admin
from django.conf.urls import patterns, url
from . import views

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^search/$', views.search, name='search'),
	url(r'^search/(?P<place_url>[-!\w]+)$', views.search, name='search'),
	url(r'^restaurants/(?P<rest_url>[-!\w]+)/$', views.restaurant, name='restaurant'),
	url(r'^signup/$', views.register, name='register'),
)
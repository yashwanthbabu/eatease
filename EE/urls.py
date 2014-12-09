from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	url(r'', include('main.urls')),
	url(r'^admin/', include(admin.site.urls)),
)
# For static media, e.g. profile pictures. Don't need this right now
if settings.DEBUG:
	urlpatterns += patterns(
		'django.views.static',
		(
			r'media/(?P<path>.*)',
			'serve',
			{'document_root': settings.MEDIA_ROOT},
		),
	)
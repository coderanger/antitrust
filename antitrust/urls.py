from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic.simple import redirect_to

import antitrust.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', antitrust.views.index, name='index'),
    url(r'^pi/$', antitrust.views.pi, name='pi'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^favicon.ico$', redirect_to, {'url': settings.STATIC_URL+'favicon.ico'}),
)

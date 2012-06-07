from django.conf.urls import patterns, include, url
from django.contrib import admin

import antitrust.views

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', antitrust.views.index, name='index'),
    url(r'^admin/', include(admin.site.urls)),
)

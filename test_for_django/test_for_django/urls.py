from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test/', include('blog.urls')),
    url(r'^sql/', include('sql_injection.urls')),
    url(r'^xss/', include('xss.urls')),
    url(r'^$','blog.views.home',name='home'),
    # url(r'^blog/',include('blog.urls')),
)

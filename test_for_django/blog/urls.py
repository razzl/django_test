from django.conf.urls import patterns, include, url

# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^$','blog.views.home',name='home'),
    # url(r'^blog/',include('blog.urls')),
    url(r'^$','blog.views.home'),
    url(r'^(?P<id>\d+)/$', 'blog.views.detail', name='detail'),
    url(r'^(?P<tag_name>\w+)/$', 'blog.views.get_articles', name='get_articles'),
)
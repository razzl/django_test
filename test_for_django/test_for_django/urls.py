from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'test_for_django.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^add/$','test_app.views.add',name='add'),
    #url(r'^$','test_app.views.index',name='home'),
    # url(r'^add/(\d+)/(\d+)/$','test_app.views.add',name='add'),
    # url(r'^$','test_app.views.home',name='home'),
    url(r'^admin/', include(admin.site.urls)),
    # url(r'^testdb/$','people.views.testdb',name='testdb'),
    # url(r'^search_form/$','people.views.search_form',name='search_form'),
    # url(r'^search/$','people.views.search',name='search'),
    # url(r'^search-post/$','people.views.search_post',name='search-post'),
)

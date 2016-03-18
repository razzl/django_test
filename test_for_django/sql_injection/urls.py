from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^(?P<name>\w+)/$', 'sql_injection.views.get_user', name='get_user'),
    url(r'^$', 'sql_injection.views.get_user', name='get_user'),
)
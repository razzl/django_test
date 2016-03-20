from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    # url(r'^(?P<name>\w+)/$', 'sql_injection.views.get_user', name='get_user'),
    url(r'^1/$', 'sql_injection.views.get_user', name='get_user'),
    url(r'^2/$', 'sql_injection.views.get_user_2', name='get_user_2'),
)    
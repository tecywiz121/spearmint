from django.conf.urls import patterns, include, url
from django.views.generic.simple import direct_to_template
from django.contrib.auth.decorators import login_required
from .views import activate, deactivate, status

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spearmint.views.home', name='home'),
    # url(r'^spearmint/', include('spearmint.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^$', login_required(direct_to_template), kwargs={'template': 'chips/index.html'}),
    url(r'^activate/$', activate, name='chips_activate'),
    url(r'^deactivate/$', deactivate, name='chips_deactivate'),
    url(r'^users.xml$', status, name='chips_status'),
)

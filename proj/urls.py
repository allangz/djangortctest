from django.conf.urls import patterns, url, include
from django.views.generic.base import RedirectView
from django.core.urlresolvers import reverse_lazy

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    #url(r'^.*$', RedirectView.as_view(url='/demo/', permanent=False), name='index'),
    url(r'^$', RedirectView.as_view(url='demo/'), name='index'),
    url(r'^demo/', include('demoapp.urls', namespace = "demo"), name='demo'),
)

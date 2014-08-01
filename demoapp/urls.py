from django.conf.urls import patterns, url
from demoapp.views import HomePageView, contact, quote, quotertc

urlpatterns = patterns('',    
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^contact/$', contact, name='contact'),
    url(r'^price/$', quote, name='price'),
    url(r'^pricertc/$', quotertc, name='pricertc'),
)

from django.conf.urls.defaults import url, include, patterns, handler404, handler500

from flyingcircus import views

urlpatterns = patterns('',
    url('^$', views.index, name='index'),
)
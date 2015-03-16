from django.conf.urls import patterns, include, url
from django.contrib import admin
#from insert.views import HelloTemplate
from insert import views

urlpatterns = patterns('',

#	url(r'^hello/$','insert.views.hello'),
#	url(r'^hello_template/$','insert.views.hello_template'),
#	url(r'^hello_template_simple/$','insert.views.hello_template_simple'),
#	url(r'^hello_class_view/$',HelloTemplate.as_view()),
    url(r'^insert/', include('insert.urls')),
   # url(r'^create/$','insert.views.create'),

    #url(r'^$', insert.views.ListView.as_view(),name='events-list'),
   	url(r'^admin/', include(admin.site.urls)),
)
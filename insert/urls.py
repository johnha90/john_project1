from django.conf.urls import patterns,include, url

from insert import views

#from insert.views import updateEL

urlpatterns = patterns('',


	url(r'^all/$', views.event),
	url(r'^input/$', views.home),
	#url(r'^event/(?P<pk>\d+)/$', updateEL.as_view(), name='event_update'),
	#url(r'^get/(?P<event_id>\d+)/$',views.event),
#    url(r'^$', insert.views.ListView.as_view(),name='events-list'),
    #url(r'^hello/$','insert.views.hello'),
    #url(r'^hello_template/$','insert.views.hello_template'),
   #url(r'^$', views.index, name='index'),
   #url(r'^(?P<event_id>\d+)/$', views.detail, name='detail'),

)
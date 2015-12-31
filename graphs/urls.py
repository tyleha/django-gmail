from django.conf.urls import patterns, url


import graphs.views as views



urlpatterns = patterns('',
    url(r'^$', views.frontpage, name="frontpage"),
    url(r'^credentials/$', views.credentials, name="credential_form"),
	url(r'^credentials/diurnal/$', views.diurnal, name="diurnal"),
	#url(r'^simple.png/$', views.simple, name="diurnal_graph"),
	url(r'^(?P<address>\w+)/(?P<password>\w+)/simple.png/$', views.simple, name="simple_graph"),
	url(r'^(?P<address>\w+)/(?P<password>\w+)/(?P<daysback>\d+)/diurnal.png/$', views.diurnal_plot, name="diurnal_graph"),


	url(r'^blahblah/(?P<property>\w+)/$', views.argpassing, name='blah'),

	url(r'^time/$', views.current_datetime, name="time_view"),
)
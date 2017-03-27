from django.conf.urls import url,include

from . import views

app_name = 'polls'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^drop/$', views.CreateMyModelView.as_view(), name='drop'),
    url(r'^events/$', views.EventsView.as_view(), name='events'),
    url(r'^events/single/$', views.EventSingleView.as_view(), name='eventsingle'),
    url(r'^events/average/$', views.EventAverageView.as_view(), name='eventaverage'),
    url(r'^events/single/(?P<eventid>[\w-]+)/$', views.EventSingleRankView, name='eventsinglepage'),
    url(r'^events/average/(?P<eventid>[\w-]+)/$', views.EventAverageRankView, name='eventaveragepage'),
    url(r'^events/competitions/$', views.UpcomingCompsView, name='upcomingcomps'),
    url(r'^events/competitions/(?P<compid>[\w-]+)/$', views.CompView, name='comp'),

]

from django.conf.urls import url


import views


urlpatterns = [
    url(r'^list/$', views.JobSpecListView.as_view(), name="list"),
    url(r'^create/$', views.JobSpecCreateView.as_view(), name="create"),
    url(r'^detail/(?P<pk>[^/]+)/$', views.JobSpecDetailView.as_view(),
        name='detail'),
    url(r'^routecard_generate/(?P<pk>[^/]+)/$', views.RouteCardGenerateModalCreateView.as_view(),
        name='routecard_generate'),
    url(r'^edit/(?P<pk>[^/]+)/$', views.JobSpecDetailEditView.as_view(),
        name='edit'),
    url(r'^processcreate/(?P<pk>[^/]+)/$', views.ProcessModalCreateView.as_view(),
        name='processcreate'),

]

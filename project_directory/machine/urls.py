from django.conf.urls import url


import views


urlpatterns = [
    url(r'^list/$', views.MachineListView.as_view(), name="list"),
    url(r'^create/$', views.MachineModalCreateView.as_view(), name="create"),
    url(r'^getMachine/$',
        views.getMachine, name="getMachine"),
    url(r'^machine_plans/(?P<pk>[^/]+)/$',
        views.MachineDetailView.as_view(), name="machine_plans"),
    url(r'^edit/(?P<pk>[^/]+)/$', views.MachineDetailEditView.as_view(),
        name='edit'),

]

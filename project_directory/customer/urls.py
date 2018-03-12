from django.conf.urls import url


import views


urlpatterns = [
    url(r'^list/$', views.CustomerListView.as_view(), name="list"),
    url(r'^create/$', views.CustomerModalCreateView.as_view(), name="create"),
    url(r'^(?P<pk>[^/]+)/detail/$', views.CustomerDetailView.as_view(),
        name='detail'),
    url(r'^(?P<pk>[^/]+)/edit/$', views.CustomerEditView.as_view(),
        name='edit'),
]

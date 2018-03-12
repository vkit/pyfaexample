from django.conf.urls import url


import views


urlpatterns = [
    url(r'^list/$', views.ProcessListView.as_view(), name="list"),
    url(r'^processcreate/$', views.ProcessModalCreateView.as_view(), name="processcreate"),
    url(r'^processnamecreate/$', views.ProcessNameModalCreateView.as_view(), name="processnamecreate"),
]

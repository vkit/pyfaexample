from django.conf.urls import url


import views


urlpatterns = [
    url(r'^list/$', views.OperatorsListView.as_view(), name="list"),
    url(r'^create/$', views.OperatorModalCreateView.as_view(), name="create"),
]

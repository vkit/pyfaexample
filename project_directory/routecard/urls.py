from django.conf.urls import url


import views


urlpatterns = [
    url(r'^list/$', views.RouteCardListView.as_view(), name="list"),
    url(r'^create/$', views.RouteCardModalCreateView.as_view(), name="create"),
    url(r'^detail/(?P<pk>[^/]+)/$', views.RouteCardDetailView.as_view(),
        name='detail'),
    url(r'^plancreate/(?P<pk>[^/]+)/$', views.PlanModalCreateView.as_view(),
        name='plancreate'),
    url(r'^planlist/$', views.PlanListView.as_view(), name="planlist"),
    url(r'^operator_planlist/$',
        views.OperatorMachineListView.as_view(), name="operator_planlist"),
    url(r'^plan_detail/(?P<pk>[^/]+)/$',
        views.OperatorPlanDetailView.as_view(),
        name='plan_detail'),
    url(r'^edit_routecard/(?P<pk>[^/]+)/$',
        views.RouteCardDetailEditView.as_view(),
        name='edit_routecard'),
    url(r'^report_detail/(?P<pk>[^/]+)/$',
        views.OperatorRouteCardReportDetailView.as_view(),
        name='report_detail'),
    url(r'^routecardreportcreate/(?P<pk>[^/]+)/$',
        views.OperatorRouteCardReportModalCreateView.as_view(),
        name='routecardreportcreate'),
    url(r'^replan/$', views.RePlanView.as_view(),
        name='replan'),

    # print all the plans
    url(r'^printplan/(?P<pk>[^/]+)/$',
        views.PrintPLanView.as_view(),
        name='printplan'),
]

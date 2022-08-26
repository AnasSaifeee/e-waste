from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='myapp'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("signin",views.signin, name='signin'),
    path("signup",views.signup, name='signup'),
    path("profile", views.profile, name='profile'),
    path("dform", views.dform, name='dform'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("guidelines",views.guidelines,name='guidelines'),
    path("notifications",views.notifications,name='notifications'),
    path("requestcollector",views.requestcollector,name='requestcollector'),
    path("login2",views.login2,name='login2'),
    path("order_details",views.order_details,name='order_details'),
    path("dashboard2",views.dashboard2,name='dashboard2'),
     path("dashboard3",views.dashboard3,name='dashboard3'),
     path("dashboard4",views.dashboard4,name='dashboard4'),
     path("post",views.post,name='post'),
     path("searchngo",views.searchngo,name='searchngo'),
    path("events",views.events,name='events'),
    path("notifications2",views.notifications2,name='notifications2')
]

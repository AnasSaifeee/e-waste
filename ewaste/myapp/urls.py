from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("index", views.index, name='myapp'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("signin",views.signin, name='signin'),
    path("signup",views.signup, name='signup'),
    path("dform", views.dform, name='dform'),
    path("dashboard", views.dashboard, name='dashboard'),
    path("guidelines",views.guidelines,name='guidelines'),
    path("notifications",views.notifications,name='notifications'),
     path("login2",views.login2,name='login2')
]
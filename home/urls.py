from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='home'),
    path("login", views.login, name='login'),
    path("logout", views.logout, name='logout'),
    path("register", views.register, name='register'),
    path("about", views.about, name='about'),
    path("services", views.services, name='services'),
    path("contact", views.contact, name='contact'), 
    path("profile", views.profile, name='profile'), 
    path("forms", views.forms, name='forms'),
    path("events", views.events, name='events'), 
    path("allevents", views.allevents, name='allevents'),     
    path("allprofiles", views.allprofiles, name='allprofiles'), 
    path("eventlogin", views.eventlogin, name='eventlogin'),
    path("allregistrations", views.allregistrations, name='allregistrations'),
]

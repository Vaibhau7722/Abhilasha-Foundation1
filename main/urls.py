from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('donation/', views.donation, name='donation'),
    path('events/', views.events, name='events'),
    path('volunteers/', views.volunteers, name='volunteers'),
]
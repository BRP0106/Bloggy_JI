from django.urls import path
from . import views  # import views

urlpatterns = [

    path('', views.Home, name='Home'),
    path('About/', views.About, name='About'),
    path('Contacts/', views.Contacts, name='Contacts'),

]

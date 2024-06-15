from django.contrib import admin
from django.urls import path, include
from . import views # import views
urlpatterns = [

    path('', views.Profiles, name='Profile'),
    path('Login/', views.Login, name='Login'),
    path('LoginForm/', views.LoginForm, name='LoginForm'),
    path('Logout/', views.Logout, name='Logout'),
    path('Registrations/', views.Registrations, name='Registrations'),
    path('RegistrationForm/', views.RegistrationForm, name='RegistrationForm'),
    path('ForgotPassword/', views.ForgotPassword, name='ForgotPassword'),
    path('ForgotPasswordForm/', views.ForgotPasswordForm, name='ForgotPasswordForm'),
    path('EditProfile/<int:id>/', views.EditProfile, name='EditProfile'),

]

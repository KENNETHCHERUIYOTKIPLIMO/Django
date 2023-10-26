from . import views
from django.urls import path

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('contact/', views.contact, name='contact'),
  path('classes/', views.classes, name='classes'),
  path('services/', views.services, name='services')

  ]
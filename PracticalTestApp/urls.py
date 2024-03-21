from django.urls import path
from PracticalTestApp import views

app_name = 'PracticalTestApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name ='about')
]
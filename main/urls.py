from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='Home'),
    path('<int:pk>', views.index, name='Single'),
    path('create', views.create, name='Create')
]
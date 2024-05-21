from django.urls import path

from Talar import views

urlpatterns = [
    path('', views.index, name='index'),
]
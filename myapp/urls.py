from django.urls import path
from .import views
urlpatterns=[
    path('',views.home,name='home'),
    path('must/',views.must),
    path('home/',views.home),
    path('food/',views.food),
    path('register/',views.register),
]
from django.urls import path 

from page.views import *

urlpatterns = [
    path('', indexView, name='index'),
    path('route/<str:page>', routeView, name='route'),
]
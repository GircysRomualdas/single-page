from django.urls import path 

from page.views import *

urlpatterns = [
    path('', indexView, name='index'),
]
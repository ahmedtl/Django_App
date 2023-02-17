from django.urls import path
from .views import *

urlpatterns = [
    path('e',index),
    path('list',list),
]
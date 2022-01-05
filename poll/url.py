from django.urls import path
from . views import *

urlpatterns = [
    path("results/<int:pk>",results,name='results'),
    path("vote/<int:pk>",vote,name='vote'),
    path("create",create,name='create'),
    path("",home,name='home'),
]
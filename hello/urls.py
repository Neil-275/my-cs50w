from django.urls import path
from . import views

urlpatterns = [
    path ("",views.main,name="main"),
    path ("<str:name>",views.index, name="index"),
]
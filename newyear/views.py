from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.
def index(request):
    now=datetime.datetime.now()
    # var=""
    # if (now.month==1 and now.day==1):
    #         var="YES"
    # else:
    #      var="NO"
    return render(request,"newyear/index.html",{
        "var":now.month==1 and now.day==1
        })
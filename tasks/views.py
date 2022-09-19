from audioop import reverse
from http.client import HTTPResponse
from django.shortcuts import render
from django import forms
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse

tasks=[]

# Create your views here.

class newTaskForm (forms.Form):
    task= forms.CharField(label="New Task")

def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []

    return render(request, "tasks/index.html",{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = newTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            request.session["tasks"] += [task]
            return HttpResponseRedirect(reverse("tasks:index"))
            # return render(request, "tasks/index.html",{
            #     "tasks":tasks
            # })
        else :
            return render(request,"tasks/add.html",{
                "form":form
            })

    return render (request,"tasks/add.html",{
        "form": newTaskForm()
    })
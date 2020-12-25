from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("<h1>Hi, this is fscohort Home page.</h1>")


def about_view(request):
    return HttpResponse("Hi ,this is fscohort about page.")

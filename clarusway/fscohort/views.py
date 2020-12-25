from django.shortcuts import render
from django.http import HttpResponse


def home_view(request):
    return HttpResponse("Hi, this is fscohort Home page.")


def about_view(request):
    return HttpResponse("Hi ,this is fscohort about page.")

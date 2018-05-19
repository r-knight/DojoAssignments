from django.shortcuts import render, HttpResponse, redirect

def new(request):
    response = "placeholder for users to create a new user record"
    return HttpResponse(response)

def display(request):
    response = "placeholder to display all the users"
    return HttpResponse(response)

def login(request):
    response = "placeholder for users to login"
    return HttpResponse(response)
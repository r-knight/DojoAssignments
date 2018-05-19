from django.shortcuts import render, HttpResponse, redirect

def index(request):
    request.session['name'] ="This is a test name"
    response = "placeholder to later display the list of blogs"
    return HttpResponse(response)

def new(request):
    response = "placeholder to later display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
        print("*"*50)
        print(request.POST)
        print(request.POST['name'])
        print(request.POST['desc'])
        request.session['name'] = "test"
        request.session['counter'] = 100
        print("*"*50)
        return redirect('/blogs')
    else:
        return redirect('/blogs')

def show(request):
    response = "placeholder to display blog {{number}}"
    return HttpResponse(response)

def edit(request):
    response = "placeholder to edit blog {{number}}"
    return HttpResponse(response)

def destroy(request):
    return redirect('/blogs')
from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    response="index placeholder"
    return render(request, "users/index.html", {'users': User.objects.all()})

def new(request):
    response="new placeholder"
    return render(request, "users/new.html")

def edit(request, uid):
    response="edit placeholder"
    user=User.objects.get(id=uid)
    context = {
        'first_name': user.first_name,
        'last_name' : user.last_name,
        'email' : user.email,
        'id' : user.id,
    }
    request.session['edit_id'] = context['id']
    return render(request, "users/edit.html", { 'user': context })

def show(request, uid):
    user=User.objects.get(id=uid)
    context = {
        'first_name': user.first_name,
        'last_name' : user.last_name,
        'email' : user.email,
        'id' : user.id,
    }
    return render(request, "users/show.html", { 'user': context })

def create(request):
    if request.method == "POST":
        if request.POST['first_name']:
            request.session['first_name'] = request.POST['first_name']
        if request.POST['last_name']:
            request.session['last_name'] = request.POST['last_name']
        if request.POST['email']:
            try:
                exists = User.objects.get(email=request.POST['email'])
            except User.DoesNotExist:
                request.session['email'] = request.POST['email']
        if request.POST['first_name'] and request.POST['last_name'] and request.POST['email']: 
            user = User(first_name= request.session['first_name'], last_name = request.session['last_name'], email = request.session['email'])
            user.save()
            newId = user.id
        return redirect("/users/" + str(newId))
    else:
        return redirect('/users/')

def destroy(request, uid):
    u = User.objects.get(id = uid)
    u.delete()
    return redirect("/users/")

def update(request):
    if request.method == "POST":
        uid = request.session['edit_id']
        u = User.objects.get(id=uid)
        request.session.pop('first_name')
        request.session.pop('last_name')
        request.session.pop('email')
        if request.POST['first_name']:
            request.session['first_name'] = request.POST['first_name']
        if request.POST['last_name']:
            request.session['last_name'] = request.POST['last_name']
        if request.POST['email']:
            try:
                exists = User.objects.get(email=request.POST['email'])
                if (exists == u):
                    request.session['email'] = request.POST['email']
                else:
                    request.session['email'] = u.email #if email already exists, don't change the email
            except User.DoesNotExist:
                request.session['email'] = request.POST['email']
        if request.POST['first_name'] and request.POST['last_name'] and request.POST['email']: 
            u.first_name = request.session['first_name']
            u.last_name = request.session['last_name']
            u.email = request.session['email']
            u.save()
            url = "/users/" + str(u.id)
            return redirect(url)
        else:
            return redirect("/users/" + str(id) +"/edit") 
    else:
        return redirect('/users/')


from django.shortcuts import render, redirect, HttpResponse
from .models import *

def index(request):
    return render(request, 'login_reg_flow/index.html')
def register(request):
    if request.method == 'POST':
        errors = User.objects.basic_validator(request.session, request.POST)
        if len(errors) == 0:
            u = User.objects.register_new_user(request.session, request.POST)
            return redirect('users/success')
        else:
            print("Found " + str(len(errors)) + " errors!")
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
    else:
        return redirect('/')
def login(request):
    if request.method == 'POST':
        user = User.objects.validate_login(request.session, request.POST)
        if user:
            return redirect('users/success')
        else:
            messages.error(request, "The email and password provided do not match any records in our database")
            return redirect('/')
    else:
        return redirect('/')
def success(request):
    if 'id' in request.session:
        return redirect('/users/'+str(request.session['id']))
    else:
        return redirect('/')
def logout(request):
    if 'id' in request.session:
        request.session.pop('id')
    return redirect('/')
def view_user(request, user_id):
    if len(User.objects.filter(id=user_id)) > 0:
        user = User.objects.get(id=user_id)
        reviews = user.review_set.all()
        return render(request, 'login_reg_flow/view_user.html', {'user':user, 'reviews':reviews})
    else:
        response = "placeholder for view_user page for user " + str(user_id) +". User does not exist yet!"
        return HttpResponse(response)
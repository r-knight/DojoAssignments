from django.shortcuts import render, redirect, HttpResponse
from .models import *
import bcrypt
import re

r = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
def isValidEmail(email):
    if len(email) > 7:
        if re.match(r, email) != None:
            return True
    return False

def index(request):
    return render(request, 'login_reg_flow/index.html')
def register(request):
    if request.method == 'POST':
        errorCount = 0
        if (request.POST['alias']):
            request.session['alias'] = request.POST['alias']
            if len(request.session['alias']) < 2:
                errorCount +=1
        else:
            errorCount += 1
        if (request.POST['name']):
            request.session['name'] = request.POST['name']
            if len(request.session['name']) < 2:
                errorCount +=1
        else:
            errorCount += 1
        if (request.POST['email']):
            request.session['email'] = request.POST['email']
            if not isValidEmail(request.session['email']):
                errorCount+=1
            elif len(User.objects.filter(email=request.session['email'])) > 0:
                errorCount+=1
        else:
            errorCount += 1
        if (request.POST['password']):
            if len(request.POST['password']) < 8:
                errorCount +=1
            elif request.POST['password'].isalpha():
                errorCount +=1
            elif request.POST['password'] == request.POST['password'].lower():
                errorCount +=1
            else: 
                hash1 = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
                if (request.POST['password_confirm']):
                    if not bcrypt.checkpw(request.POST['password_confirm'].encode(), hash1):
                        errorCount +=1
                else:
                    errorCount += 1
        else:
            errorCount += 1
        if errorCount == 0:
            u = User(first_name = request.session['alias'], last_name = request.session['name'], email=request.session['email'], pwhash=hash1)
            u.save()
            print("No errors!")
            request.session.clear()
            request.session['id'] = u.id
            return redirect('users/success')
        else:
            print("Found " + str(errorCount) + " errors!")
            return redirect('/')
    else:
        return redirect('/')
def login(request):
    if request.method == 'POST':
        request.session['e_email'] = request.POST['e_email']
        if len(User.objects.filter(email = request.session['e_email'])) > 0:
            user = User.objects.get(email = request.session['e_email'])
            if request.POST['e_password']:
                if bcrypt.checkpw(request.POST['e_password'].encode(), user.pwhash.encode()):
                    request.session.clear()
                    request.session['id'] = user.id
                    return redirect('users/success')
        else:
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
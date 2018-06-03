from django.shortcuts import render, redirect, HttpResponse

def index(request):
    response = "placeholder for index"
    return render(request, 'users/index.html')
def signin(request):
    response = "placeholder for signin"
    return render(request, 'users/signin.html')
def register(request):
    response = "placeholder for register"
    return render(request, 'users/register.html')
def logoff(request):
    response = "placeholder for logoff"
    request.session.clear()
    return redirect('/')
def show(request, id):
    response = "placeholder for show for user " + str(id)
    return render(request, 'users/show.html', {'id':id})
def edit(request):
    response = "placeholder for edit"
    return render(request, 'users/edit.html')
def new(request):
    response = "placeholder for new"
    return render(request, 'users/new.html')
def edit_admin(request, id):
    response = "placeholder for edit_admin for user " + str(id)
    return render(request, 'users/edit_admin.html', {'id':id})
def post_comment(request):
    response = "placeholder for post_comment"
    return HttpResponse(response)
def post_message(request):
    response = "placeholder for post_message"
    return HttpResponse(response)

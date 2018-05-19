from django.shortcuts import render, redirect


def index(request):
    return render (request, 'surveys/index.html')


def process(request):
    if request.method == "POST":
        if request.POST['name']:
            request.session['name'] = request.POST['name']
        if request.POST['location']:
            request.session['location'] = request.POST['location']
        if request.POST['language']:
            request.session['language'] = request.POST['language']
        if request.POST['comment']:
            request.session['comment'] = request.POST['comment']
        if 'counter' in request.session:
            request.session['counter'] = request.session['counter'] +1
        else:
           request.session['counter'] = 1
        if request.POST['name'] and request.POST['location'] and request.POST['language']:
            return redirect ('/result')
        else:
            return redirect ('/')
    else:
        return redirect ('/')

def result(request):
    return render(request, 'surveys/result.html', words = request.session['words'])
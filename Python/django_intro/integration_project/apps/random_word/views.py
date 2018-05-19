from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string


def index(request):
    if 'counter' not in request.session:
        request.session['counter'] = 1
    if 'word' not in request.session:
        request.session['word'] = get_random_string(length=14)
    response = "testing?"
    #return HttpResponse(response)
    return render (request, 'random_word/index.html')

def reset(request):
    try:
        del request.session['counter']
    except keyError as e:
        pass
    return redirect('/')

def new(request):
    request.session['counter'] = request.session['counter'] + 1
    request.session['word'] = get_random_string(length=14)
    return redirect('/')
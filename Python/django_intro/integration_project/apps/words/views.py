from django.shortcuts import render, redirect
import time

def index(request):
    return render(request, 'words/index.html')

def process(request):
    if request.method == "POST":
        size = request.POST.get('checkbox_big', False);
        if size == False :
            size = 'normal'
        curr_time = time.gmtime()
        if request.POST['new_word'] != "":
            request.session['word'] = request.POST['new_word']
            print("Got word! Word: ", request.session['word'])
        else:
            print("No word detected")
            return redirect('/')
        request.session['color'] = request.POST['color']
        if 'words' in request.session:
            request.session['words'].append({'word': request.session['word'], 'color': request.session['color'], 'size': size, 'timestamp': time.strftime("%c", curr_time)})
        else:
            request.session['words'] = [{'word': request.session['word'], 'color': request.session['color'], 'size': size, 'timestamp': time.strftime("%c", curr_time)}]
        return redirect('/new')
    else:
        return redirect('/')

def new(request):
        return redirect('/')

def reset(request):
        request.session.clear()
        return redirect('/')
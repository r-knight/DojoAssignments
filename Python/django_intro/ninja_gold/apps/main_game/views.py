from django.shortcuts import render, redirect
from random import randint
import datetime

def index(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    if 'activities' not in request.session:
        request.session['activities'] = []
    return render(request, 'main_game/index.html')

def process_money(request, string):
    print("Got request to process")
    print(string)
    if string=='casino':
        dGold = randint(-50,50)
        print('in casino!')
    elif string=='cave':
        dGold = randint(5,10)
        print('in cave!')
    elif string=='house':
        dGold = randint(2,5)
        print('in house!')
    elif string=='farm':
        dGold = randint(10,20)
        print('in farm!')
    else:
        print('in unknown location!')
        return redirect ('/')
    request.session['gold'] += int(dGold)
    if dGold >= 0:
        result = 'won'
    else:
        result = 'lost'
    request.session['activities'].append({'gold': abs(dGold), 'location':string, 'result': result, 'timestamp': datetime.datetime.utcnow().strftime("%A, %B %d %y %I:%M%p") })
    return redirect('/processed')

def processed(request):
    print("Processed request")
    return redirect('/')
    
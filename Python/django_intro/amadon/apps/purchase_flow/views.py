from django.shortcuts import render, redirect

item_prices = {'1001': 19.99, '1002':29.99, '1003': 4.99, '1004':49.99}

def index(request):
    return render(request, 'purchase_flow/index.html')

def buy(request):
    if request.method == 'POST':
        request.session['item_id'] = request.POST['product_id']
        request.session['quantity'] = request.POST['quantity']
        request.session['order_total'] = item_prices[request.session['item_id']] * int(request.session['quantity'])
        if 'orders' in request.session:
            request.session['orders'].append({'item_id':request.session['item_id'], 'quantity': request.session['quantity'], 'order_total': request.session['order_total']})
            request.session['total_items'] += int(request.session['quantity'])
            request.session['total_purchase_amount'] += float(request.session['order_total'])
        else:
            request.session['orders'] = []
            request.session['orders'].append({'item_id':request.session['item_id'], 'quantity': request.session['quantity'], 'order_total': request.session['order_total']})
            request.session['total_items'] = int(request.session['quantity'])
            request.session['total_purchase_amount'] = float(request.session['order_total'])
        return redirect('/amadon/checkout')
    else:
        return redirect('/amadon')

def checkout(request):
    return render(request, 'purchase_flow/checkout.html')

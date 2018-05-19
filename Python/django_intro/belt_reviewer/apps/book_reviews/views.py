from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import *
from apps.login_reg_flow.models import *

def list(request):
    recent = Review.objects.all().order_by('-id')[:3]
    if 'id' in request.session:
        user = User.objects.get(id=request.session['id'])
    else:
        user = User.objects.get(id=0)
    reviews = Review.objects.all()
    books = Book.objects.filter(id__in=[review.book.id for review in reviews])
    return render(request, 'book_reviews/books.html',{'recent':recent, 'user':user, 'books': books})

def view_book(request, book_id):
    if len(Book.objects.filter(id=book_id)) > 0:
        book = Book.objects.get(id=book_id)
        request.session['last_viewed_book'] = book.id
        recent = book.review_set.all().order_by('-id')[:3]
        if 'id' in request.session:
            user = User.objects.get(id=request.session['id'])
        else:
            user = User.objects.get(id=0)
        return render(request, 'book_reviews/view_book.html', {'book': book, 'recent':recent, 'user':user})
    else:
        response = "Book with ID " + str(book_id) + " not found!<a href='/books'>Back to list</a>"
        return HttpResponse(response)

def add(request):
    authors = Author.objects.all()
    return render(request, 'book_reviews/add.html', {'authors': authors})

def process_book(request):
    if request.method == 'POST':
        errors = Book.objects.basic_validator(request.session, request.POST)
        if len(errors) == 0:
            review = Book.objects.submit_review(request.session)
            if review:
                return redirect('/books/' + str(review.book.id))
            else:
                return redirect('/books/add')
        else:
            for key, value in errors.items():
                messages.error(request, value)
                print (value)
            print ("Found " + str(len(errors)) + " errors!")
            return redirect('/books/add')
 
    else:
        response = "This page can only be access with a POST method!"
        return HttpResponse(response)

def review_existing(request):
    if request.method == 'POST':
        errors = Book.objects.validate_review_for_existing(request.session, request.POST)
        if len(errors) == 0:
            #submit review
            review = Book.objects.submit_review_for_existing(request.session)
            if review:
                return redirect('/books/' + str(review.book.id))
            else:
                return redirect('/books/' + str(request.session['last_viewed_book']))
        else:
            print ("Found " + str(len(errors)) + " errors!")
            for key, value in errors.items():
                messages.error(request, value)
                print (value)
            if 'last_viewed_book' in request.session:
                return redirect('/books/' + str(request.session['last_viewed_book']))
            else:
                return redirect('/books/add')
    else:
        response = "This page can only be access with a POST method!"
        return HttpResponse(response)

def destroy(request, review_id):
    if 'id' in request.session:
        review = Review.objects.delete_selected(request.session, review_id)
        if review:
            if 'last_viewed_book' in request.session:
                return redirect('/books/' + str(request.session['last_viewed_book']))
            else:
                return redirect('/books/add')
        else:
            response = "You can't delete another user's reviews!"
            return HttpResponse(response)
    else:
        response = "You must be logged in to delete a review!"
        return HttpResponse(response)
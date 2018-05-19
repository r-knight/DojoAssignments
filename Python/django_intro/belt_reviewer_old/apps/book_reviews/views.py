from django.shortcuts import render, redirect, HttpResponse
from .models import *
from apps.login_reg_flow.models import *

def list(request):
    return render(request, 'book_reviews/books.html')
def view_book(request, book_id):
    if len(Book.objects.filter(id=book_id)) > 0:
        book = Book.objects.get(id=book_id)
        request.session['last_viewed_book'] = book.id
        recent = book.review_set.all().order_by('-id')[:3]
        if 'id' in request.session:
            user = User.objects.get(id=request.session['id'])
        return render(request, 'book_reviews/view_book.html', {'book': book, 'recent':recent, 'user':user})
    else:
        response = "Book with ID " + str(book_id) + " not found!<a href='/books'>Back to list</a>"
        return HttpResponse(response)

def add(request):
    authors = Author.objects.all()
    return render(request, 'book_reviews/add.html', {'authors': authors})

def process_book(request):
    if request.method == 'POST':
        errorCount = 0
        if request.POST['title']:
            request.session['title'] = request.POST['title']
        else:
            errorCount +=1
        if request.POST.get('existing_author'):
            request.session['author'] = request.POST['existing_author']
        else:
            if request.POST['new_author']:
                request.session['author'] = request.POST['new_author']
            else:
                errorCount +=1
        if request.POST['review_text']:
            request.session['review_text'] = request.POST['review_text']
            if len(request.session['review_text']) < 15:
                errorCount+=1
        else:
            errorCount +=1
        if request.POST['rating']:
            request.session['rating'] = int(request.POST['rating'])
            if request.session['rating'] > 5:
                request.session['rating'] = 5
            elif request.session['rating'] < 1:
                request.session['rating'] = 1
        else:
            errorCount +=1
        if errorCount == 0:
            #submit review
            if len(Author.objects.filter(name=request.session["author"])) > 0 and len(Book.objects.filter(title=request.session['title'])) > 0:
                author = Author.objects.get(name=request.session["author"])  #This book and author both exist
                book = Author.objects.get(title=request.session['title'])
            elif len(Author.objects.filter(name=request.session["author"])) > 0:
                author = Author.objects.get(name=request.session["author"])  #Existing author, new book
                book = Book(title=request.session['title'], author=author)
                book.save()
            else:
                author = Author(name=request.session["author"])    #New book and author
                author.save()
                book = Book(title=request.session['title'], author=author)
                book.save()
            if 'id' in request.session:
                user = User.objects.get(id=request.session['id'])
            else:
                user = User.objects.get(id=0) #saves as guest account
            review = Review(description = request.session['review_text'], book = book, reviewer = user, rating = request.session['rating'])
            review.save()
            del request.session['title']
            del request.session['review_text']
            del request.session['author']
            del request.session['rating']
            return redirect('/books/' + str(review.book.id))
        else:
            print ("Found " + str(errorCount) + " errors!")
            return redirect('/books/add')
 
    else:
        response = "This page can only be access with a POST method!"
        return HttpResponse(response)

def review_existing(request):
    if request.method == 'POST':
        errorCount = 0
        if 'last_viewed_book' in request.session:
            request.session['book'] = request.session['last_viewed_book']
        else:
            errorCount +=1
        if request.POST['review_text']:
            request.session['review_text'] = request.POST['review_text']
            if len(request.session['review_text']) < 15:
                errorCount+=1
        else:
            errorCount +=1
        if request.POST['rating']:
            request.session['rating'] = int(request.POST['rating'])
            if request.session['rating'] > 5:
                request.session['rating'] = 5
            elif request.session['rating'] < 1:
                request.session['rating'] = 1
        else:
            errorCount +=1
        
        if errorCount == 0:
            #submit review
            if 'id' in request.session:
                user = User.objects.get(id=request.session['id'])
            else:
                user = User.objects.get(id=0) #saves as guest account
            book = Book.objects.get(id=request.session['book'])
            review = Review(description = request.session['review_text'], book = book, reviewer = user, rating = request.session['rating'])
            review.save()
            del request.session['book']
            del request.session['review_text']
            del request.session['rating']
            return redirect('/books/' + str(review.book.id))
        else:
            print ("Found " + str(errorCount) + " errors!")
            return redirect('/books/add')
 
    else:
        response = "This page can only be access with a POST method!"
        return HttpResponse(response)

def destroy(request, review_id):
    if 'id' in request.session:
        review = Review.objects.get(id=review_id)
        book_id = review.book_id
        if request.session['id'] == review.reviewer_id:
            review.delete()
            return redirect('/books/' + str(book_id))
        else:
            response = "You can't delete another user's reviews!"
            return HttpResponse(response)
    else:
        response = "You must be logged in to delete a review!"
        return HttpResponse(response)
from django.db import models
from apps.login_reg_flow.models import *

class BookManager(models.Manager):
    def basic_validator(self, ReqSession, ReqPost):
        errors = {}
        errorCount = 0
        if ReqPost['title']:
            ReqSession['title'] = ReqPost['title']
        else:
            errors['title_blank'] = "Title must not be blank!"
            errorCount +=1
        if ReqPost.get('existing_author') and ReqPost['existing_author'] != "":
            ReqSession['author_id'] = ReqPost['existing_author']
            print("Using existing author")
        else:
            if ReqPost['new_author']:
                ReqSession['author_name'] = ReqPost['new_author']
            else:
                print("Invalid author!")
                errors['author'] = "You must select an existing author or enter a new author!"
                errorCount +=1
        if ReqPost['review_text']:
            ReqSession['review_text'] = ReqPost['review_text']
            if len(ReqSession['review_text']) < 15:
                errors['review_length'] = "Your review must be at least 15 characters!"
                errorCount+=1
        else:
            errors['review_blank'] = "Your review must not be blank!"
            errorCount +=1
        if ReqPost['rating']:
            ReqSession['rating'] = int(ReqPost['rating'])
            if ReqSession['rating'] > 5:
                ReqSession['rating'] = 5
            elif ReqSession['rating'] < 1:
                ReqSession['rating'] = 1
        else:
            errors['rating'] = "You must leave a review between 1 and 5 stars!"
            print("Invalid rating!")
            errorCount +=1
        if 'author_name' in ReqSession:
            print("Author Name: " + ReqSession['author_name'])
        elif 'author_id' in ReqSession:
            print("Author ID: " + str(ReqSession['author_id']))
        else:
            print("nani?!")
        return errors
    def validate_review_for_existing(self, ReqSession, ReqPost):
        errorCount = 0
        errors = {}
        if 'last_viewed_book' in ReqSession:
            ReqSession['book'] = ReqSession['last_viewed_book']
        else:
            errors['no_book'] = "Data for last viewed book not found. Cookies must be enabled to review a book!"
            errorCount +=1
        if ReqPost['review_text']:
            ReqSession['review_text'] = ReqPost['review_text']
            if len(ReqSession['review_text']) < 15:
                errors['review_length'] = "Your review must be at least 15 characters!"
                errorCount+=1
        else:
            errors['review_blank'] = "Your review must not be blank!"
            errorCount +=1
        if ReqPost['rating']:
            ReqSession['rating'] = int(ReqPost['rating'])
            if ReqSession['rating'] > 5:
                ReqSession['rating'] = 5
            elif ReqSession['rating'] < 1:
                ReqSession['rating'] = 1
        else:
            errors['invalid_rating'] = "Your review must include a valid rating!"
            errorCount +=1
        return errors
    def submit_review(self, ReqSession):
        #submit review
        if 'author_id' in ReqSession: #existing author
            if len(Book.objects.filter(title=ReqSession['title'])) > 0:
                author = Author.objects.get(id=ReqSession["author_id"])  #existing book
                book = Book.objects.get(title=ReqSession['title'])
            else:
                author = Author.objects.get(id=ReqSession["author_id"])  #new book
                book = Book(title=ReqSession['title'], author=author)
                book.save()
        elif 'author_name' in ReqSession: #new author, must be a new book
            author = Author(name=ReqSession["author_name"])    #New book and author
            author.save()
            book = Book(title=ReqSession['title'], author=author)
            book.save()
        else:
            #edge case of session variables with author not saving properly, or if they are deleted between validating and submitting
            errors['invalid_author'] = "Your review must include a valid author!"
            return False
        if 'id' in ReqSession:
            user = User.objects.get(id=ReqSession['id'])
        else:
            user = User.objects.get(id=0) #saves as guest account if id is not found in session
        review = Review(description = ReqSession['review_text'], book = book, reviewer = user, rating = ReqSession['rating'])
        review.save()

        del ReqSession['title']
        del ReqSession['review_text']
        if 'author_id' in ReqSession:
            del ReqSession['author_id']
        elif 'author_id' in ReqSession:
            del ReqSession['author_name']
        del ReqSession['rating']

        return review
    def submit_review_for_existing(self, ReqSession):
        if 'id' in ReqSession:
            user = User.objects.get(id=ReqSession['id'])
        else:
            user = User.objects.get(id=0) #saves as guest account
        book = Book.objects.get(id=ReqSession['book'])
        review = Review(description = ReqSession['review_text'], book = book, reviewer = user, rating = ReqSession['rating'])
        review.save()

        del ReqSession['book']
        del ReqSession['review_text']
        del ReqSession['rating']

        return review

class ReviewManager(models.Manager):
    def delete_selected(self, ReqSession, review_id):
        review = Review.objects.get(id=review_id)
        book_id = review.book_id
        if ReqSession['id'] == review.reviewer_id:
            review.delete()
            return True
        else:
            return False

class Author(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()

class Review(models.Model):
    description = models.TextField(default="")
    book = models.ForeignKey(Book)
    reviewer = models.ForeignKey('login_reg_flow.User')
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = ReviewManager()

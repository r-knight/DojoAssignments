from django.db import models

class Author(models.Model):
    name = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Book(models.Model):
    title = models.CharField(max_length = 255)
    author = models.ForeignKey(Author)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Review(models.Model):
    description = models.TextField(default="")
    book = models.ForeignKey(Book)
    reviewer = models.ForeignKey('login_reg_flow.User')
    rating = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

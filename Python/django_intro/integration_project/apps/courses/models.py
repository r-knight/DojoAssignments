from __future__ import unicode_literals
from django.db import models
from ..login_reg_flow.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Description(models.Model):
    text = models.CharField(max_length = 255)
    course = models.OneToOneField(Course, related_name="description")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)


class Users_Courses(models.Model):
    student = models.ForeignKey(User)
    course = models.ForeignKey(Course)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    
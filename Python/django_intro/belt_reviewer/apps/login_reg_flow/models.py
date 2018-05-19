from django.db import models
import bcrypt
import re

r = "(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
def isValidEmail(email):
    if len(email) > 7:
        if re.match(r, email) != None:
            return True
    return False

class UserManager(models.Manager):
    def basic_validator(self, ReqSession, ReqPost):
        errors = {}
        if (ReqPost['alias']):
            ReqSession['alias'] = ReqPost['alias']
            if len(ReqSession['alias']) < 2:
                errors['alias_too_short'] = "Alias must be 2 or more characters!"
        else:
            errors['alias_blank'] = "Alias must not be blank!"
        if (ReqPost['name']):
            ReqSession['name'] = ReqPost['name']
            if len(ReqSession['name']) < 2:
                errors['name_too_short'] = "Name must be 2 or more characters!"
        else:
            errors['name_blank'] = "Name must not be blank!"
        if (ReqPost['email']):
            ReqSession['email'] = ReqPost['email']
            if not isValidEmail(ReqSession['email']):
                errors['email_invalid'] = "Email must be valid!"
            elif len(User.objects.filter(email=ReqSession['email'])) > 0:
                errors['email_already_registered'] = "An account with that email already exists!"
        else:
            errors['email_blank'] = "Email must not be blank!"
        if (ReqPost['password']):
            if len(ReqPost['password']) < 8:
                errors['password_short'] = "Password must be at least 8 characters!"
                
            elif ReqPost['password'].isalpha():
                errors['password_all_letters'] = "Password must contain at least one number or special character!"
                
            elif ReqPost['password'] == ReqPost['password'].lower():
                errors['password_all_lowercase'] = "Password must contain at least one uppercase letter!"
                
            else: 
                hash1 = bcrypt.hashpw(ReqPost['password'].encode(), bcrypt.gensalt())
                if (ReqPost['password_confirm']):
                    if not bcrypt.checkpw(ReqPost['password_confirm'].encode(), hash1):
                        errors['password_mismatch'] = "Password and password confirm must match!"                        
                else:
                    errors['password_confirm_blank'] = "Password confirmation must not be blank!"
        else:
            errors['password_blank'] = "Password must not be blank!"
        return errors
    def register_new_user(self, ReqSession, ReqPost): 
            hash1 = bcrypt.hashpw(ReqPost['password'].encode(), bcrypt.gensalt())
            u = User(alias = ReqSession['alias'], name = ReqSession['name'], email=ReqSession['email'], pwhash=hash1)
            u.save()
            print("No errors!")
            ReqSession.clear()
            ReqSession['id'] = u.id
            return True
    def validate_login(self, ReqSession, ReqPost):
        ReqSession['e_email'] = ReqPost['e_email']
        if len(User.objects.filter(email = ReqSession['e_email'])) > 0:
            user = User.objects.get(email = ReqSession['e_email'])
            if ReqPost['e_password']:
                if bcrypt.checkpw(ReqPost['e_password'].encode(), user.pwhash.encode()):
                    ReqSession.clear()
                    ReqSession['id'] = user.id
                    return user
            return False
        else:
            return False
        
class User(models.Model):
    name = models.CharField(max_length = 255)
    alias = models.CharField(max_length = 255)
    email = models.CharField(max_length = 255)
    pwhash = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
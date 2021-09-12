from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 30)
    mobile = models.CharField(max_length = 30)
    landline = models.CharField(max_length = 30)
    email = models.CharField(max_length = 30)
    fax = models.CharField(max_length = 30)
    ownerId = models.BigIntegerField()

class Token(models.Model):
    ownerId = models.BigIntegerField()
    token = models.CharField(max_length = 200)
    time = models.BigIntegerField()

class Login(models.Model):
    username = models.CharField(max_length = 30)
    hashedpassword = models.CharField(max_length = 300)
    ownerId = models.BigIntegerField()


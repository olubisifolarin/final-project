from ast import mod
import email
from email.mime import image
from django.db import models
from random import choices


# Create your models here.    
    
class Profile(models.Model):
    username = models.CharField(max_length=20)
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    email = models. EmailField()
    
    def __str__(self):
        return self.firstname
        
    
    
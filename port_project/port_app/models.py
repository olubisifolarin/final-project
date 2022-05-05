from distutils.command.upload import upload
from email import message
from operator import mod
from tabnanny import verbose
from django.urls import reverse
from tkinter import CASCADE
from turtle import title
from django.db import models
from django.contrib.auth.models import User
import datetime
from django.utils.text import slugify
from tinymce.models import HTMLField


# Create your models here.
class Resume(models.Model):
    year = models.CharField(max_length=20, unique=True)
    title = models.CharField(max_length=50, unique=True)
    subtitle = models.CharField(max_length=50, unique=True)
    content = models.TextField()

    def __str__(self):
        return self.title

class Skill(models.Model):
    name = models.CharField(max_length=20, unique=True)
    title = models.IntegerField()


class Blog(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(unique=True)
    image = models.ImageField(blank=True, null=True, upload_to='upload/pics')
    created = models.DateTimeField(null=True)
    content = HTMLField('Content')   
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    
    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.title)
            super(Blog, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    def image_url(self):
        if self.image: 
            return self.image.url
        
class Comment(models.Model):
    name = models.CharField(max_length=30)
    create_on =  models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)
    parent = models.ForeignKey("self", null=True, blank=True, on_delete=models.CASCADE, related_name='replies')  
                               
    class Meta:
        ordering = [ '-create_on']

    def __str__(self):
        return self.name
    
# class Reply(models.Model):
#     name = models.CharField(max_length=30)
#     create_on =  models.DateTimeField(auto_now_add=True)
#     content = models.TextField()
#     post = models.ForeignKey(Blog, related_name='comments', on_delete=models.CASCADE)
    
#     class Meta:
#         verbose_name_plural = "replies"

#     def __str__(self):
#         return self.name
    
    @property
    def children(self):
        return Comment.objects.filter(parent=self)
    
    @property
    def is_parent(self):
        if self.parent is not None:
            return False
        return True

class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()
    subject =models.CharField(max_length=60)
    message = models.TextField()

    def __str__(self):
        return self.name
    

class Testi(models.Model):
    content = models.TextField()
    name = models.CharField(max_length=30)
    title = models.CharField(max_length=20)
    image = models.ImageField(blank=True, null=True, upload_to='upload/pics')
    
    def __str__(self):
        return self.content

    


    


    
    
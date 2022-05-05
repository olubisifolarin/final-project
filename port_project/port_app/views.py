from imaplib import _Authenticator
from re import template
import re
from site import USER_BASE
from statistics import mode
from unicodedata import name
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from port_app.models import *
from django.views.generic import ListView, DetailView, FormView
from port_app.models import Blog
from port_app.form import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import update_session_auth_hash

# Create your views here.


def index(request):
    port = Resume.objects.all()
    blog = Blog.objects.order_by('-created')[:3]
    skill = Skill.objects.all()
    testi = Testi.objects.all()
    
    if request.method == 'POST':
        contact_form = ContactForm(request.POST)
        if contact_form.is_valid():
            contact_form.save(commit=False)
            return redirect('index')           
    else:
        contact_form = ContactForm()
    return render(request, 'port_app/index.html', {'port': port, 'blog':blog, 'skill': skill, 'contact': contact_form, 'reg': register, 'testi': testi}) 


def blog(request):
    blogs = Blog.objects.order_by('created') 
    return render(request, 'port_app/blog.html', {'blogs':blogs})

# class blog_detail(DetailView):
#     model = Blog
#     template_name = 'port_app/single.html'
#     content_object_name = 'detail_blog'   
    

def blog_detail(request, slug):
    detail_blog = get_object_or_404(Blog, slug=slug)
    comments = Comment.objects.filter(post__slug=slug).order_by('-create_on')
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False) 
            comment.post =  detail_blog             
            comment.save()
        return redirect(reverse('port_app:detail_blog', kwargs={'slug':slug}))
    
    else:
        form = CommentForm()
    return render(request, 'port_app/single.html', {'comm':comments, 'form':form, 'detail_blog':detail_blog})


# def blog_detail(request, slug):
#     detail_blog = get_object_or_404(Blog, slug=slug)
#     replies = Reply.objects.filter(post__slug=slug).order_by('-create_on')
#     if request.method == "POST":
#         replies = ReplyForm(request.POST)
#         if form.is_valid():
#             replies = form.save(commit=False) 
#             replies.post =  detail_blog             
#             replies.save()
#         return redirect(reverse('port_app:detail_blog', kwargs={'slug':slug}))
    
#     else:
#         form = ReplyForm()
#     return render(request, 'port_app/single.html', {'reply':replies})


def  register(request):
    if request.method =='POST':
        reg = RegisterForm(request.POST)
        if reg.is_valid():
            user = reg.save()
            login(request, user)
            return redirect("backend:signin")
    else:
        reg = RegisterForm()      
    return render(request, 'port_app/register.html', {'reg': reg})

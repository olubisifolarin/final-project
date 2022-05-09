from audioop import add
import http
from urllib import response
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponse
from backend.form import *
from django.contrib import messages
from backend.models import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout






# Create your views here.          
def signin(request):
    if request.method == 'POST':
        username = request.POST['user_name']
        password = request.POST['password']
            
        user = authenticate(request, username=username, password=password)
            
        if user is not None:
            login(request, user)
            return redirect('backend:dashboard')
    else:
        messages.error(request, 'Wrong Information')
    return render(request, 'backend/signin.html')
 
 
 
@login_required(login_url='/signin/')
def dashboard(request):
    return render(request, 'backend/dashboard.html')

@login_required(login_url='/signin/')
def view_profile(request):
    view_profile = Profile.objects.filter()
    return render(request, 'backend/view-profile.html', {'profile':view_profile})

@login_required(login_url='/signin/')
def edit_profile(request):
    if request.method == 'POST':
        edit_profile = EditProfileForm(request.POST, instance=request.user)
        if edit_profile.is_valid():
            edit_profile.save()
            messages.success(request, 'Profile Edited Successfully')
            return redirect('backend:edit_profile')
    else:
            edit_profile=EditProfileForm()
    return render(request, 'backend/edit-profile.html', {'edit_pro':edit_profile})

@login_required(login_url='/signin/')
def view_blog(request):
    view_blog = Blog.objects.filter(user=request.user) 
    return render(request, 'backend/view-blog.html', {'view':view_blog})

@login_required(login_url='/signin/')
def add_blog(request):
    if request.method == 'POST':
        blog = AddBlogForm(request.POST,request.FILES)
        if blog.is_valid():        
            blog.save()
            blog = AddBlogForm()
            messages.success(request, 'Blog Posted')
    else:
        blog = AddBlogForm()
    return render(request, 'backend/add-blog.html', {'blog':blog})

# for dashboard blog edit, view and delete

@login_required(login_url='/signin/')
def edit_post(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug)
    if request.method == 'POST':
        editform =EditBlogForm(request.POST, request.FILES, instance=single_blog)
        if editform.is_valid():
            blogf = editform.save(commit=False)
            blogf.user = request.user
            blogf.save()
            # messages.success(request, 'Blog Edit Successfully')
            return redirect('backend:view_blog')
        
    else: 
        editform = EditBlogForm(instance=single_blog)
    return render(request, 'backend/edit-blogpost.html', {'edit':editform})



# def edit_post(request, slug):
#     editpost = get_object_or_404(Blog, slug=slug)
#     if request.method == 'POST':
#         form = EditBlogForm(request.POST, request.FILES, instance=editpost)   
#         if form.is_valid():
#             editpost = form.save(commit=False)
#             editpost.save()          
#             messages.success(request, 'Blog Edited Successfully')
#             return redirect('backend:view_blog')             
#     else:
#         form = EditBlogForm(instance=editpost)
#         return render(request, 'backend/edit-blogpost.html', {'form':form})

@login_required(login_url='/signin/')
def view_post(request, slug):
    view_blogpost = get_object_or_404(Blog, slug=slug)
    return render(request, 'backend/viewblog_post.html', {'post':view_blogpost})
    
@login_required(login_url='/signin/')
def delete_post(request, slug):
    post_record = get_object_or_404(Blog, slug=slug)
    post_record.delete()
    return redirect('backend:view_blog')

@login_required(login_url='/signin/')
def password_change(request):
    if request.method == 'POST':
        pass_form = PasswordChangeForm(data=request.POST,
        user=request.user)
        if pass_form.is_valid():
            pass_form.save()
            update_session_auth_hash(request, pass_form.user)
            messages.success(request, 'Password changed successfully.')
    else:
        pass_form = PasswordChangeForm(user=request.user)
    return render(request, 'backend/change_password.html', {'pass_key':pass_form})

@login_required(login_url='/signin/')
def signout(request):
    logout(request)
    return redirect('backend:signin')
                

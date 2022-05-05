from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core import validators
from django.contrib.auth.models import User
from port_app.models import*



class EditProfileForm(forms.ModelForm):
    username = forms.CharField(label='Username :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username', 'style': 'color:white;'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname', 'style': 'color:white;'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname', 'style': 'color:white;'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control', 'placeholder': 'Upload you pics', 'style': 'color:white;'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email', 'style': 'color:white;'}))
    
    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email']
        
        
class AddBlogForm(forms.ModelForm):
    title = forms.CharField(label='Title :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your title', 'style': 'color:white;'}))
    
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control', 'placeholder': 'Upload your pics', 'style': 'color:white;'}))
    content = forms.CharField(label='Content :',
                             widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content', 'style': 'color:white;'}))
    
    
    class Meta():
        model = Blog
        fields = ['title', 'image', 'content', 'user']
        exclude = ['created', 'slug']
        
    # How to edit our blogpost(Form)
class EditBlogForm(forms.ModelForm):

    content = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Edit post', 'style': 'color:white;'}))
    class Meta():
        model = Blog
        exclude = ['slug', 'blog_title', 'created', 'user']
        
class ViewBlogPostForm(forms.ModelForm):
    
    title = forms.CharField(label='Title :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter your title', 'style': 'color:white;'}))
    image = forms.ImageField(required=False, widget=forms.FileInput(
        attrs={'class': 'form-control', 'placeholder': 'Upload your pics', 'style': 'color:white;'}))
    content = forms.CharField(label='Content :',
                             widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Content', 'style': 'color:white;'}))
    
    class Meta():
        model = Blog
        exclude = ['slug', 'user']
        
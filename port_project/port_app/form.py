from email import message
from tkinter.ttk import Style
from django import forms
from port_app.models import Comment, Contact
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.core import validators
from django.contrib.auth.models import User





class CommentForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
        
    }))
    class Meta:
        model = Comment
        exclude = ['create_on', 'post', 'active', 'parent']
        
class ReplyForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Full Name'}))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4'
    }))
    class Meta:
        model = Comment
        exclude = ['create_on', 'post']


class ContactForm(forms.ModelForm):

    name = forms.CharField( widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Your Name', 'style': 'width:100%;'}))
    email = forms.EmailField( widget=forms.EmailInput(attrs={'class':'form_control', 'placeholder': 'Your Email', 'style': 'width:100%;'}))
    subject = forms.CharField( widget=forms.TextInput(attrs={'class': 'form_control', 'placeholder': 'Subject', 'style': 'width: 100%;'}))
    message = forms.CharField( widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': ' Enter Your Message',
        'id': 'usercontact',
        'rows': '4'
    }))
    class Meta():
        model = Contact
        fields= '__all__'
       
class RegisterForm(UserCreationForm):
    username = forms.CharField(label='Username :', widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Username'}))
    first_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Firstname'}))
    last_name = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Lastname'}))
    email = forms.EmailField(label='Email :',
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    password1 = forms.CharField(label='Enter Password :', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    
    def clean_email(self):
        email_field = self.cleaned_data.get('email')
        if User.objects.filter(email=email_field).exists():
            raise forms.ValidationError('Email already exist')
        return email_field

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']

        if commit:
            user.save()
            return user


   
    
    
class change_password(PasswordChangeForm):
        
    password1 = forms.CharField(label='Enter Password :', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Password'}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
  
    class Meta():
        model: PasswordChangeForm
        fields = '__all__'
        


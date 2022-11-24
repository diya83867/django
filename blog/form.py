from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('author','title', 'text', 'thumbnail_image', 'feature_image','category','tag')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'mobile_number', 'mail','company','designation','state','country','about','image')

class User_Update(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','mobile_number','mail','company','designation','state','country','about','image')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'comment')

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', 'description')

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ('name', 'description', 'tag_image')

class LoginForm(forms.Form):
    mail = forms.CharField(label='username or mail')
    password = forms.CharField(widget=forms.PasswordInput)

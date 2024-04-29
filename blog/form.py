from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *

class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('title', 'text', 'thumbnail', 'featured','category','tag')

class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email','company','designation','state','country','about','image')

class User_Update(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name','email','company','designation','state','country','about','image')

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
        fields = ('name', 'description', 'image')

class LoginForm(forms.Form):
    mail = forms.CharField(label='username or mail')
    password = forms.CharField(widget=forms.PasswordInput)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'

class WorkUpdateForm(forms.ModelForm):
    class Meta:
        model = WorkUpdate
        fields = '__all__'

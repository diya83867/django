import http
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
)
import httplib2
from django.conf import settings
from .seriallizer import *
from .models import *
from .form import *
import csv

def register(request):
    if request.method == 'POST':
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        designation = request.POST["designation"]
        company = request.POST["company"]
        email = request.POST["email"]
        image = request.FILES["image"]
        about = request.POST["about"]
        state = request.POST["state"]
        country = request.POST["country"]
        if User.objects.filter(username=username).exists():
            messages.warning(request, 'This account is already exists.')
        else:
            user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name,designation=designation,image=image,about=about,state=state,country=country,company=company)
            user = authenticate(username=user.username, password=password)
            login(request, user)
            messages.success(request, 'User created Successfully.')
            return redirect("blog:post_list")
    return render(request, 'blog/register.html')     

def loginUser(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            user = User.objects.get(email=username)
        except:
            user = None
        if user is not None:    
            user = authenticate(username=user.username, password=password)
            if user.is_active:
                login(request, user)
                return redirect("blog:post_list")
        else:
            return HttpResponse("error")
    return render(request, "blog/login.html")

def getfile(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="file.csv"'
    users = User.objects.all()
    writer = csv.writer(response)
    for user in users:
        writer.writerow([user.username, user.first_name, user.last_name, user.email])
    return response

def view_profile(request):
    profile = User.objects.all()
    context = {'profile': profile}
    return render(request, 'blog/view_profile.html', context)

def edit_profile(request):
    if request.method == 'POST':
        form = User_Update(request.POST, request.FILES, instance=request.user)
        update = form.save(commit=False)
        update.user = request.user
        update.save()
        return redirect('/profile/')
    else:
        form = User_Update(instance=request.user)
    return render(request, 'blog/edit_profile.html', {'form': form})


def logoutUser(request):
    logout(request)
    return redirect("/")

def post_list(request):
    if request.user.is_authenticated:
        posts = Post.objects.filter(publish__lte=timezone.now(), author=request.user).order_by("-id")
        return render(request, 'blog/post_list.html', {'posts': posts})
    else:
        posts = Post.objects.filter(publish__lte=timezone.now()).order_by("?")[:10]
        return render(request, 'blog/post_list.html', {'posts': posts})

def post_detail(request, slug):
    posts = get_object_or_404(Post, slug=slug)
    comments = posts.comments.filter(parent__isnull=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            reply_obj = None
            reply_id = None
            reply_id = request.POST.get('reply_id')
            if reply_id:
                reply_obj = Comment.objects.filter(id=reply_id).last()
            if reply_id:
                reply_comment = form.save(commit=False)
                reply_comment.parent = reply_obj
                reply_comment.post = posts
                reply_comment.user = request.user
                reply_comment.save()
            response = form.save(commit=False)
            response.post = posts
            response.user = request.user
            response.save()
            return redirect('blog:post_detail', slug=slug)
    else:
        form = CommentForm()
    return render(request, 'blog/post_details.html', {'posts': posts, 'comments': comments, 'form': form})

def category_list(request):
    categorys = Category.objects.all()
    return render(request, 'blog/category_list.html', {'categorys': categorys})

def category_detail(request, slug):
    categorys = get_object_or_404(Category, slug=slug)
    post = Post.objects.filter(category=categorys)
    return render(request, 'blog/category_detail.html', {'posts': post})

def tag_list(request):
    tags = Tag.objects.all()
    return render(request, 'blog/tag_list.html', {'tags': tags})

def tag_detail(request, slug):
    tags = get_object_or_404(Tag, slug=slug)
    post = Post.objects.filter(tag=tags)
    return render(request, 'blog/tag_detail.html', {'posts': post})

def loop(request):
    a = []
    for i in range(26):
        if i != 0:
            a.append(i)
    return render(request, 'blog/loop.html', {"a":a})

def addPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm()
    return render(request, 'blog/post_new.html', {'form': form})

def post_edit(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            form.save_m2m()
            return redirect('blog:post_detail', slug=post.slug)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form, 'post':post})

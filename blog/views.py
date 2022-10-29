from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login, authenticate, logout
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import (
	HTTP_400_BAD_REQUEST,
	HTTP_404_NOT_FOUND,
	HTTP_200_OK
)
from .seriallizer import *
from rest_framework.authtoken.models import Token
from .models import *
from .form import *
import csv

# Create your views here.

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def mobileNotificationList(request):
	tokenkey = request.data.get("tokenKey")
	try:
		token = Token.objects.get(key=tokenkey)
	except:
		return Response({'error': "Invalid Token Key"},status=HTTP_200_OK)
	user = token.user
	notificationList = userNotification.objects.filter(user = user).order_by('-id')
	notificationListSerialized = userNotificationSerializer(notificationList,many=True)
	return Response({ 'notificationList' : notificationListSerialized.data},status=HTTP_200_OK)

@csrf_exempt
@api_view(['GET', 'POST'])
@permission_classes((AllowAny,))
def mobileNotificationDetail(request):
    tokenkey = request.data.get("tokenKey")
    id = request.data.get("id")
    try:
        token = Token.objects.get(key=tokenkey)
    except:
        return Response({'error': "Invalid Token Key"},status=HTTP_200_OK)
    user = token.user
    notificationList = userNotification.objects.filter(id = id).last()
    return Response(notificationList.data)


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

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'blog/register.html', context)

def loginUser(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            mail = form.cleaned_data['mail']
            password = form.cleaned_data['password']
            try:
                the_user = User.objects.get(username=mail)
            except User.DoesNotExist:
                the_user = User.objects.get(mail=mail)
            except:
                the_user = None
            if the_user is not None:    
                user = authenticate(username = the_user.username, password = password)
                if user.is_active:
                    login(request, user)
                    return redirect("/")
    form = LoginForm()
    context = {'form': form, 'title': "Login"}
    return render(request, "blog/login.html", context)

def logoutUser(request):
    logout(request)
    return redirect("/")

def post_list(request):
    posts = Post.objects.filter(
        published_date__lte=timezone.now()).order_by("published_date")
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
            print(reply_id)
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

def post_new(request):
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

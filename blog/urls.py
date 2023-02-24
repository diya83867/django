from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('post/<str:slug>/edit/', views.post_edit, name='post_edit'),

    path('add-post', views.addPost, name='addPost'),
    path('post/<str:slug>/', views.post_detail, name='post_detail'),
    path('category/<slug:slug>/', views.category_detail, name='category_detail'),
    path('tag/<slug:slug>/', views.tag_detail, name='tag_detail'),

    path("loop/", views.loop, name="loop"),
    path("register/", views.register, name="register"),
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('category/', views.category_list, name='category_list'),
    path('tag/', views.tag_list, name='tag_list'),
    path("profile/", views.view_profile, name="view_profile"), 
    path("edit/", views.edit_profile, name="edit_profile"),
    path('csv/',views.getfile),

    path('', views.post_list, name='post_list'),
]

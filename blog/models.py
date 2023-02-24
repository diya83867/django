from django.contrib.auth.models import AbstractUser
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from autoslug.fields import AutoSlugField
from ckeditor_uploader.fields import RichTextUploadingField

class User(AbstractUser):
    parent = models.ForeignKey("self", verbose_name="Parent", on_delete=models.PROTECT, blank=True, null=True)  
    number = models.IntegerField(validators=[MinValueValidator(5000000000),MaxValueValidator(999999999999)], default=5000000000)
    company = models.CharField(max_length=50)
    designation = models.CharField(max_length=100)
    state = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    about = models.TextField(max_length=300)
    image = models.ImageField(upload_to='user_image')

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='cat_image')
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    image = models.ImageField(upload_to='tag_image')
    slug = AutoSlugField(populate_from='name', unique=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    category = models.ForeignKey(Category , on_delete=models.PROTECT, related_name='blog_category')
    title = models.CharField(max_length=100)
    slug = AutoSlugField(max_length=200, editable=False, populate_from='title', unique=True, null=True)
    text = RichTextUploadingField()
    thumbnail = models.ImageField(upload_to='thumbnail_image')
    featured = models.ImageField(upload_to='feature_image')
    tag = models.ManyToManyField(Tag, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    publish = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.PROTECT, related_name='comments')
    parent = models.ForeignKey('self', on_delete=models.PROTECT, related_name='replies')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment = models.CharField(max_length=50)

    def __str__(self):
        return self.name
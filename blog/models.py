from django.db import models
from django.utils import timezone
from autoslug import AutoSlugField
from django.contrib.auth.models import AbstractUser, User

class User(AbstractUser):
    mobile_number = models.IntegerField()
    email = models.EmailField(null=True,blank=True)
    mail = models.EmailField()
    company = models.CharField(max_length=50,null=True)
    designation = models.CharField(max_length=50,null=True)
    state = models.CharField(max_length=10,null = True)
    country = models.CharField(max_length=10,null=True)
    about = models.CharField(max_length=200,null=True)
    image = models.ImageField(upload_to='user_image/',null=True,blank=True)

class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    cat_image = models.ImageField(upload_to='cat_image', null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)

    def __str__(self):
        return self.name + " - " + self.description

class Tag(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    tag_image = models.ImageField(upload_to='tag_image', null=True, blank=True)
    slug = AutoSlugField(populate_from='name', unique=True, null=True)

    def __str__(self):
        return self.name + "-" + self.description

class Post(models.Model):
    author = models.ForeignKey(User ,on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=300)
    description = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    thumbnail_image = models.ImageField(upload_to='thumbnail_image', null=True, blank=True)
    feature_image = models.ImageField(upload_to='feature_image', null=True, blank=True)
    category = models.ForeignKey(Category , on_delete=models.CASCADE, blank=True, null=True, related_name='blog_category')
    tag = models.ManyToManyField(Tag, blank=True)
    slug = AutoSlugField(max_length=200, editable=False, populate_from='title', unique=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    comment = models.CharField(max_length=50)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True, related_name='replies')

    def __str__(self):
        return self.name

from django.db import models
from django.utils import timezone
from autoslug.fields import AutoSlugField
from django.contrib.auth.models import AbstractUser, User
from ckeditor_uploader.fields import RichTextUploadingField

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
    smsMessage = models.TextField(null=True, blank=True)

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
    text = RichTextUploadingField()
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

class userNotification(models.Model):
	user = models.ForeignKey(User,related_name='studentNT',on_delete=models.CASCADE)
	title = models.TextField(null=True, blank=True)
	message = models.TextField(null=True, blank=True)
	image = models.FileField(upload_to ='Notification/',null=True, blank=True)
	timestamp = models.DateTimeField(auto_now_add=True, editable=False)
	utimestamp = models.DateTimeField(auto_now=True, editable=False)

	class Meta:
		verbose_name_plural = 'Mobile-Notifications'

	def __str__(self):
		return self.user.username +"-"+self.title or '--Title not provided--'

class m2mUpdate(models.Model):
    title = models.TextField(null=True, blank=True)
    m2m = models.ManyToManyField(Tag, blank=True)
    number = models.IntegerField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'm2m-update'

    # def save(self):
    #     if self.id:
    #         data = m2mUpdate.objects.filter(id=self.id)
    #         tag = Tag.objects.filter(id__in=list(set(data.values_list('m2m', flat=True)))).all()
    #         d1 = m2mUpdate.objects.get(id=self.id)
    #         d1.m2m.clear()
    #     super(m2mUpdate,self).save()

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
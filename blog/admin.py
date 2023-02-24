from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import csv

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    search_fields = ('name', 'email')
    list_display = ('name', 'email', 'comment')
    list_filter = ['name', 'email']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)

class CustomUserAdmin(UserAdmin):
    actions = ["export_as_csv"]
    list_display = ('username', 'email', 'is_superuser')

    def export_as_csv(self, request, queryset):
        meta = self.model._meta
        field_names = [field.name for field in meta.fields]
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}.csv'.format(meta)
        writer = csv.writer(response)
        writer.writerow(field_names)
        for obj in queryset:
            row = writer.writerow([getattr(obj, field) for field in field_names])
        return response

    list_filter = ('company', 'state', 'country')
    search_fields = ('first_name', 'last_name', 'company', 'state', 'country')

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category')
    list_display = ('title', 'category', 'created', 'publish')
    list_filter = ['publish', 'created']
    filter_horizontal = ('tag',)

    def view_on_site(self, obj):
        url = reverse('blog:post_detail', kwargs={'slug': obj.slug})
        return url

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']

class TagAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name']
    list_filter = ['name']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
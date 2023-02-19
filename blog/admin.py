from django.contrib import admin
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

class UserAdmin(admin.ModelAdmin):
    actions = ["export_as_csv"]
    list_display = ('username', 'email', 'mail', 'is_superuser')

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

    list_filter = ('mail', 'company', 'state', 'country')
    search_fields = ('first_name', 'last_name', 'mail', 'company', 'state', 'country')

class PostAdmin(admin.ModelAdmin):
    search_fields = ('title', 'category')
    list_display = ('title', 'category', 'created_date', 'published_date')
    list_filter = ['published_date', 'created_date']
    filter_horizontal = ('tag',)

    def view_on_site(self, obj):
        url = reverse('blog:post_detail', kwargs={'slug': obj.slug})
        return url

class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_display = ('name', 'description')
    list_filter = ['name', 'description']

class TagAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')
    list_display = ('name', 'description')
    list_filter = ['name', 'description']

admin.site.register(User, UserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(userNotification)

class m2mUpdateAdmin(admin.ModelAdmin):
    filter_horizontal = ('m2m',)

admin.site.register(m2mUpdate, m2mUpdateAdmin)
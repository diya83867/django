from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.admin.models import LogEntry
from django.http import HttpResponse
from django.urls import reverse
from .models import *
import csv

class LogEntryAdmin(admin.ModelAdmin):
	list_display = ['user', 'content_type', 'action_flag', 'object_id', 'object_repr', 'action_time']
	search_fields = ['user__username','content_type__model']
	readonly_fields = ('content_type', 'user', 'action_time', 'object_id', 'object_repr', 'action_flag', 'change_message' )

	def has_delete_permission(self, request, obj=None):
		return False

	def get_actions(self, request):
		actions = super(LogEntryAdmin, self).get_actions(request)
		if 'delete_selected' in actions:
			del actions['delete_selected']
		return actions

	def has_add_permission(self,request):
		return False

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
            writer.writerow([getattr(obj, field) for field in field_names])
        return response

    list_filter = ('company', 'state', 'country')
    search_fields = ('first_name', 'last_name', 'company', 'state', 'country')

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide', 'extrapretty'),
    #         'fields': ('first_name', 'last_name', 'email', 'number', 'username', 'password1', 'password2', ),
    #     }),
    # )
    # fieldsets = [
    #     (None, {'fields': ('email', 'username', 'number', 'first_name', 'last_name', 'password',)}),
    #     ('Personal info', {'fields': ("parent","company","designation","state","country","email","about","image")}),
    #     ('Permissions', {'classes': ('collapse', ), 'fields': ('is_active','is_staff','is_superuser','groups','user_permissions')}),
    #     ('Important dates', {'classes': ('collapse', ), 'fields': ('last_login','date_joined')}),
    # ]

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

class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['name']
    list_display = ['name', 'created']

class WorkUpdateAdmin(admin.ModelAdmin):
    search_fields = ['employee__name', 'details']
    list_display = ['employee', 'details', 'created']
    autocomplete_fields = ['employee']

admin.site.register(User, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(WorkUpdate, WorkUpdateAdmin)

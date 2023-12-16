from django import template
from blog.models import Employee

register = template.Library()

@register.filter
def employees(data):
    return Employee.objects.all()
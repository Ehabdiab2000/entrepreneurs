from django.contrib import admin

# Register your models here.
from .models import Project , Join

admin.site.register(Project)
admin.site.register(Join)


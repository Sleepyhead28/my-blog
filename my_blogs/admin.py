from django.contrib import admin

# Register your models here.

from .models import Category, Topic, Entry

admin.site.register(Category)
admin.site.register(Topic)
admin.site.register(Entry)

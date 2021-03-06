from django.contrib import admin
from .models import Bb

# Register your models here.

class BbAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'price', 'published')
    list_display_links = ('title', 'content')
    search_fields = ('title', 'content', 'price')


admin.site.register(Bb, BbAdmin)

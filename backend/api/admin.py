from django.contrib import admin

# Register your models here.
from .models import *

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'category', 'author', 'is_featured', 'status')
    search_fields = ('id', 'title', 'category', 'status')
    """ list_editable = ('list_display',) """


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
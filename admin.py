from django.contrib import admin
from blog.models import Blog, Category

class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'slug')

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')

admin.site.register(Blog, BlogAdmin)
admin.site.register(Category, CategoryAdmin)

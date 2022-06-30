from django.contrib import admin
from blogs.models import BlogsCategoryModel, BlogsModel


# Register your models here.



@admin.register(BlogsCategoryModel)
class BlogsCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(BlogsModel)
class BlogsModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']
from django.contrib import admin
from blogs.models import CategoryModel , BlogModel

# Register your models here.



@admin.register(CategoryModel)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(BlogModel)
class BLogModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']
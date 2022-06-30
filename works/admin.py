from django.contrib import admin
from works.models import WorksCategoryModel, WorksModel

# Register your models here.


@admin.register(WorksCategoryModel)
class WorksCategoryModelAdmin(admin.ModelAdmin):
    list_display = ['id','name']

@admin.register(WorksModel)
class WorksModelAdmin(admin.ModelAdmin):
    list_display = ['id','title','created_at']
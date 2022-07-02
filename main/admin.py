from django.contrib import admin
from main.models import ContactsModel
# Register your models here.



@admin.register(ContactsModel)
class ContactsModelAdmin(admin.ModelAdmin):
    list_display = ['id','name','phone','created_at']

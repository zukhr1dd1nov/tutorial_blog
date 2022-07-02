from django.db import models

# Create your models here.

class ContactsModel(models.Model):
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=13)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.TimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'контактные данные'
        verbose_name_plural = 'контактные данные'
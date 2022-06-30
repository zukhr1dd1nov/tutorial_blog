from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.

class WorksCategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория работ'
        verbose_name_plural = 'категории работ'

class WorksModel(models.Model):
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    created_at = models.TimeField(auto_now_add=True)
    categories = models.ManyToManyField(WorksCategoryModel)
    work_image = models.ImageField(upload_to='works/')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'работа'
        verbose_name_plural = 'работы'

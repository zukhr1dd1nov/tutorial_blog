from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class CategoryModel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'

class BlogModel(models.Model):
    category = models.ForeignKey(CategoryModel,on_delete=models.RESTRICT)
    title = models.CharField(max_length=255)
    body = RichTextUploadingField()
    created_at = models.TimeField(auto_now_add=True)
    image = models.ImageField(upload_to='blogs')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'блог'
        verbose_name_plural = 'блоги'
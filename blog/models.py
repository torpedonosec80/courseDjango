from django.db import models

# Create your models here.
class Category(models.Model):
    """Category model"""
    name = models.CharField("Имя", max_length=100)
    slug = models.SlugField("url", max_length=100)
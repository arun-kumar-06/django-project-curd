from django.db import models
from django.core.validators import MinLengthValidator

class Posts(models.Model):
    title = models.CharField(max_length=200,)
    slug = models.SlugField(unique=True,)
    content = models.TextField(blank=False)

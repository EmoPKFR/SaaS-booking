from django.db import models
from django.conf import settings
from django.utils.text import slugify


class Business(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='businesses'
    )
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    address = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name
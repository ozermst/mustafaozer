from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import BlogCategory, BlogTag


@receiver(pre_save, sender=BlogCategory)
def lowercase_blog_categoryname(sender, instance, **kwargs):
    instance.name = instance.name.lower()


@receiver(pre_save, sender=BlogTag)
def lowercase_blog_tag_name(sender, instance, **kwargs):
    instance.name = instance.name.lower()

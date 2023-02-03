from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    pass


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ForeignKey(
    #     "wagtailimages.Image", null=True, blank=True, on_delete=models.SET_NULL, related_name="+"
    # )
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.user.email

    class Meta:
        verbose_name = _("User profile")
        verbose_name_plural = _("User profile")

from django.db import models
import os
import uuid
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
def user_directory_path(instance, filename):
    ext = filename.split(".")[-1]
    filename = f"{uuid.uuid4()}.{ext}"
    return f"users/{instance.user.username}/{filename}"


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to=user_directory_path, blank=True)
    profile_picture_uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    profile_picture_original_name = models.CharField(max_length=255, blank=True)
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    facebook = models.URLField(blank=True, null=True)
    twitter = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    alternative_email = models.EmailField(blank=True, null=True)
    telephone = models.CharField(max_length=15, blank=True, null=True)
    cellphone = models.CharField(max_length=15, blank=True, null=True)
    whatsapp = models.CharField(max_length=15, blank=True, null=True)
    tiktok = models.URLField(blank=True, null=True)
    youtube = models.URLField(blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(
        User,
        related_name="updated_profiles",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
    )
    updated_ip_public = models.GenericIPAddressField(null=True, blank=True)
    updated_ip_local = models.GenericIPAddressField(null=True, blank=True)
    updated_host = models.CharField(max_length=255, null=True, blank=True)
    updated_os = models.CharField(max_length=255, null=True, blank=True)
    updated_browser = models.CharField(max_length=255, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.profile_picture:
            self.profile_picture = 'profile/default/profile.png'
        super().save(*args, **kwargs)


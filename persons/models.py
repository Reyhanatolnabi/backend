import uuid
import os
from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


def get_person_avatar_path(instance, filename):
    ext = filename.split(".")[-1]
    # Create random filename
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("persons/avatars", filename)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_code = models.CharField(max_length=10, unique=True, db_index=True)
    mobile = models.CharField(max_length=11, unique=True, db_index=True)
    address = models.CharField(max_length=500)
    avatar = models.ImageField(upload_to=get_person_avatar_path, null=True, blank=True)
    email_confirmed = models.BooleanField(default=False)
    mobile_confirmed = models.BooleanField(default=False)
    description = models.CharField(max_length=2000, null=True, blank=True)

    def __str__(self):
        return self.user.username

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

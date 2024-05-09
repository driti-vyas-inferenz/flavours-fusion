from django.contrib.auth.models import AbstractUser
from django.db import models

from django.utils.translation import gettext_lazy as _
from django.core.validators import validate_image_file_extension


from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    GENDER = (
        ("MALE", "MALE"),
        ("FEMALE", "FEMALE"),
        ("OTHERS", "OTHERS"),
    )

    email = models.EmailField(_("email address"), blank=True, unique=True)

    gender = models.CharField(
        verbose_name=_("Select Gender"),
        choices=GENDER,
        max_length=10,
        null=True,
        blank=True,
    )

    mobile = models.CharField(
        verbose_name=_("Mobile Number"),
        unique=True,
        max_length=20,
    )

    display_name = models.CharField(max_length=255, null=True, blank=True, unique=True)

    photo = models.ImageField(
        verbose_name=_("Profile Image"),
        upload_to="users/profile_images/",
        blank=True,
        null=True,
        validators=[validate_image_file_extension],
    )

    modified = models.DateTimeField(verbose_name=_('Modified'), auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


from django.contrib.auth.models import AbstractBaseUser
from django.core.validators import EmailValidator, RegexValidator
from .managers import MyUserManager
from django.db import models
from django.utils import timezone
import uuid
import os


def get_person_avatar_path(instance, filename):
    ext = filename.split(".")[-1]
    # create random file
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("persons/avatars", filename)


# Regular Expressions
national_code_regex = RegexValidator(regex=r"^([0-9]){10}$")
mobile_number_regex = RegexValidator(
    regex=r"09(1[0-9]|3[1-9]|2[1-9])-?[0-9]{3}-?[0-9]{4}"
)


class NotRegistered(AbstractBaseUser):
    first_name = models.CharField(max_length=200, blank=True, verbose_name="نام")
    last_name = models.CharField(
        max_length=200, blank=True, verbose_name="نام خانوادگی"
    )

    class Meta:
        abstract = True


class MyUser(NotRegistered):
    username = models.CharField(max_length=50, unique=True, verbose_name="نام کاربری")

    email = models.EmailField(
        unique=True, validators=[EmailValidator], verbose_name="ایمیل"
    )
    national_code = models.CharField(
        max_length=10,
        unique=True,
        validators=[national_code_regex],
        db_index=True,
        verbose_name="کد ملی",
    )
    mobile_number = models.CharField(
        max_length=11,
        unique=True,
        validators=[mobile_number_regex],
        db_index=True,
        verbose_name="موبایل",
    )
    address = models.CharField(max_length=250, blank=True, verbose_name="آدرس")
    description = models.CharField(
        max_length=200, blank=True, null=True, verbose_name="توضیحات"
    )
    email_confirm = models.BooleanField(default=False, verbose_name="تاییدیه ایمیل")
    mobile_confirm = models.BooleanField(
        default=False,
        verbose_name="تایدیه شماره همراه",
    )
    is_active = models.BooleanField(default=True, verbose_name="فعال")
    is_staff = models.BooleanField(default=False, verbose_name="پرسنل")
    is_admin = models.BooleanField(default=False, verbose_name="مدیر")

    avatar = models.ImageField(
        upload_to=get_person_avatar_path,
        blank=True,
        null=True,
        verbose_name="تصویر پروفایل",
    )
    created_at = models.DateTimeField(default=timezone.now, verbose_name="زمان ثبت نام")
    updated_at = models.DateTimeField(default=timezone.now, verbose_name='زمان آپدیت')

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'national_code', 'mobile_number']

    def __str__(self):
        return f"{self.username}"

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

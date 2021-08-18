from django.db import models
from persons.models import MyUser, get_person_avatar_path
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=200, verbose_name="عنوان دسته‌بندی")

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"


class Article(models.Model):
    STATUS_CHOICES = (
        ('d', 'پیش نویس'),  # draft
        ('p', 'منتشر شده'),  # publish
    )
    title = models.CharField(
        max_length=250, null=False, blank=False, verbose_name="عنوان مقاله"
    )
    category = models.ManyToManyField(Category)
    author = models.ForeignKey(
        MyUser,
        null=True,
        on_delete=models.SET_NULL,
        verbose_name="نویسنده",
        related_name='article',
    )
    avatar = models.ImageField(
        upload_to=get_person_avatar_path,
        verbose_name="تصویر مقاله",
    )
    content = models.TextField(verbose_name="محتوا")
    publish = models.DateTimeField(default=timezone.now, verbose_name="زمان انتشار")
    created_at = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(
        max_length=1, choices=STATUS_CHOICES, default='d', verbose_name="وضعیت"
    )

    def __str__(self):
        return f"{self.title}"

    class Meta:
        verbose_name = "مقاله"
        verbose_name_plural = "مقالات"

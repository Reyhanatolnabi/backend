from django.db import models
import uuid
import os
from mptt.models import MPTTModel, TreeForeignKey


def get_product_avatar_path(instance, filename):
    ext = filename.split(".")[-1]
    # create random file
    filename = "%s.%s" % (uuid.uuid4(), ext)
    return os.path.join("products/avatars", filename)


class Products(models.Model):
    STATUS_CHOICES = (
        ('a', 'available'),
        ('s', 'sold'),
    )
    name = models.CharField(max_length=200, verbose_name="نام محصول")
    description = models.CharField(max_length=250, blank=True, null=True, verbose_name="توضیحات")
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, verbose_name="وضعیت")
    picture = models.ImageField(
        upload_to=get_product_avatar_path,
        blank=True,
        null=True,
        verbose_name="تصویر محصول"
    )
    category = TreeForeignKey('Category', null=True, blank=True,on_delete=models.CASCADE)


class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', db_index=True,
                            on_delete=models.CASCADE)
    slug = models.SlugField()

    class MPTTMeta:
        order_insertion_by = ['name']

    class Meta:
        unique_together = (('parent', 'slug'),)
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

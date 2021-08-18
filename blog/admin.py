from django.contrib import admin
from .models import Article, Category

# Register your models here.
admin.site.register(Category)


class AtricleAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'author',
        'publish',
        'status',
    )


admin.site.register(Article, AtricleAdmin)

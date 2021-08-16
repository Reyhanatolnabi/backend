from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group
from .forms import MyUserChangeForm, MyUserCreationForm
from .models import MyUser


class MyUserAdmin(BaseUserAdmin):

    form = MyUserChangeForm
    add_form = MyUserCreationForm

    list_display = (
        'first_name',
        'last_name',
        'national_code',
        'email',
        'is_admin',
    )
    list_display_links = ('email',)

    list_filter = (
        "email",
        "is_admin",
        'national_code',
    )

    fieldsets = (
        (
            "کاربر",
            {
                'fields': (
                    'email',
                    'username',
                    'password',
                )
            },
        ),
        (
            'اطلاعات شخصی',
            {
                'fields': (
                    'first_name',
                    'last_name',
                    'national_code',
                    'mobile_number',
                    'description',
                    'address',
                    'created_at',
                    'updated_at',
                    'avatar',
                )
            },
        ),
        (
            'مجوز ها',
            {
                'fields': (
                    'is_admin',
                    'is_active',
                    'email_confirm',
                    'mobile_confirm',
                )
            },
        ),
    )

    add_fieldsets = (
        (
            None,
            {
                'fields': (
                    'email',
                    "username",
                    "national_code",
                    "mobile_number",
                    'password1',
                    'password2',
                ),
            },
        ),
    )

    search_fields = (
        'email',
        'national_code',
    )
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(MyUser, MyUserAdmin)
admin.site.unregister(Group)

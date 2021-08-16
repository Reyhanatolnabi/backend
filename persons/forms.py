from .models import MyUser
from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError


class MyUserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='رمز عبور', widget=forms.PasswordInput)
    password2 = forms.CharField(label='تکرار رمز عبور', widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "national_code",
            "mobile_number",
            "address",
            "description",
            "avatar",
            "created_at",
            "updated_at",
        )

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("گذرواژه ها مطابقت ندارند")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password2"])
        if commit:
            user.save()
        return user


class MyUserChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "national_code",
            "mobile_number",
            "address",
            "description",
            "email_confirm",
            "mobile_confirm",
            "is_active",
            "is_admin",
            "avatar",
            "created_at",
            "updated_at",
        )

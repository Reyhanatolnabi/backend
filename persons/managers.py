from django.contrib.auth.models import BaseUserManager


class MyUserManager(BaseUserManager):
    def create_user(self, email, username, national_code, mobile_number, password=None):
        if not email:
            raise ValueError('کاربر عزیز فیلد ایمیل یک فیلد اجباری است')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            national_code=national_code,
            mobile_number=mobile_number,
        )

        # for hashing password
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(
        self, email, username, national_code, mobile_number, password=None
    ):

        user = self.create_user(
            email=email,
            username=username,
            national_code=national_code,
            mobile_number=mobile_number,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

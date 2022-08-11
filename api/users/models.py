from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager


class UserManager(BaseUserManager):

    def create_superuser(self, email, username, first_name, last_name, password, **other_fields):
        other_fields.setdefault('is_active', True)
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)

        if other_fields.get('is_staff') is not True or other_fields.get('is_superuser') is not True:
            raise ValueError(
                'صاحب سایت باید به همه چیز دسترسی داشته باشد.')

        return self.create_user(email, username, first_name, password, **other_fields)

    def create_user(self, email, username, first_name, last_name, password, **other_fields):

        if not email:
            raise ValueError('ارائه ایمیل اجباری است.')

        user = self.model(
            email = self.normalize_email(email),
            username = username,
            first_name = first_name,
            last_name = last_name,
            **other_fields
        )
        user.set_password(password)
        user.save()
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='ایمیل', unique=True)
    username = models.CharField(verbose_name='نام کاربری', max_length=150, unique=True)
    first_name = models.CharField(verbose_name='نام', max_length=150)
    last_name = models.CharField(verbose_name='نام خانوادگی', max_length=150)
    is_active = models.BooleanField(verbose_name='فعال', default=False)
    is_staff = models.BooleanField(verbose_name='ادمین', default=False)
    is_superuser = models.BooleanField(verbose_name='صاحب سایت', default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'firstname', 'last_name']

    def __str__(self):
        return self.user_name
    
    class Meta:
        ordering = ['-id']
        verbose_name = 'کاربر'
        verbose_name_plural = 'کاربرها'
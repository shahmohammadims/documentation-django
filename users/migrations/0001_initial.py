# Generated by Django 4.1 on 2022-08-17 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='ایمیل')),
                ('username', models.CharField(max_length=150, unique=True, verbose_name='نام کاربری')),
                ('first_name', models.CharField(max_length=150, verbose_name='نام')),
                ('last_name', models.CharField(max_length=150, verbose_name='نام خانوادگی')),
                ('is_active', models.BooleanField(default=False, verbose_name='فعال')),
                ('is_staff', models.BooleanField(default=False, verbose_name='ادمین')),
                ('is_superuser', models.BooleanField(default=False, verbose_name='صاحب سایت')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربرها',
                'ordering': ['-id'],
            },
        ),
    ]
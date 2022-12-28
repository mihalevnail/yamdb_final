# Generated by Django 2.2.16 on 2022-09-24 19:05

import django.contrib.auth.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_auto_20220924_2055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='bio',
            field=models.TextField(blank=True, max_length=300, null=True, verbose_name='О себе'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(max_length=150, null=True, verbose_name='Код подтверждения'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='12345', max_length=128, null=True, verbose_name='Пароль'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='username',
            field=models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username'),
        ),
    ]
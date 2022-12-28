# Generated by Django 2.2.16 on 2022-09-29 09:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20220926_2017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='confirmation_code',
        ),
        migrations.AlterField(
            model_name='customuser',
            name='password',
            field=models.CharField(default='12345', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('user', 'user'), ('moderator', 'moderator'), ('admin', 'admin')], default='user', max_length=50, verbose_name='Роль пользователя'),
        ),
        migrations.AddConstraint(
            model_name='customuser',
            constraint=models.UniqueConstraint(fields=('username', 'email'), name='unique_username_email'),
        ),
    ]
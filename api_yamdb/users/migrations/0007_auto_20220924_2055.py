# Generated by Django 2.2.16 on 2022-09-24 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20220924_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='confirmation_code',
            field=models.CharField(default='1', max_length=150, verbose_name='Код подтверждения'),
        ),
    ]

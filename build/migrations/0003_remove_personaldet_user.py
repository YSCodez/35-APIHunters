# Generated by Django 4.0.3 on 2022-10-07 21:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('build', '0002_personaldet_delete_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personaldet',
            name='user',
        ),
    ]

# Generated by Django 5.1.4 on 2025-02-22 13:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0007_userprofile_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='wishlist',
        ),
    ]

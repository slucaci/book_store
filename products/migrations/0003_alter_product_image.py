# Generated by Django 5.1.4 on 2025-03-02 09:25

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_category_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=cloudinary.models.CloudinaryField(default='gimb955wkx4orxdovxnf', max_length=255, verbose_name='image'),
        ),
    ]

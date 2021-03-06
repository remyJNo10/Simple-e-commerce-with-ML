# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-03-30 16:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_tags',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to=b'product'),
        ),
    ]

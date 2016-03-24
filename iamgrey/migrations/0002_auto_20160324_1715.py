# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iamgrey', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='story',
            name='image',
            field=models.ImageField(upload_to=b'media/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='story',
            name='link',
            field=models.CharField(max_length=500, blank=True),
        ),
    ]

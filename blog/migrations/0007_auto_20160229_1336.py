# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20160229_1328'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to=b'media/%Y/%m/%d/', blank=True),
        ),
        migrations.AddField(
            model_name='post',
            name='image_title',
            field=models.CharField(max_length=250, blank=True),
        ),
    ]

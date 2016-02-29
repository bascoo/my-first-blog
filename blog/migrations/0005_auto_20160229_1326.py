# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20160224_1932'),
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
            field=models.CharField(default=datetime.datetime(2016, 2, 29, 12, 26, 31, 37000, tzinfo=utc), max_length=250),
            preserve_default=False,
        ),
    ]

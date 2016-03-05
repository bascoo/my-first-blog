# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(upload_to=b'media/%Y/%m/%d/', blank=True),
        ),
        migrations.AddField(
            model_name='event',
            name='image_title',
            field=models.CharField(unique=True, max_length=20, blank=True),
        ),
        migrations.AlterField(
            model_name='event',
            name='date_event',
            field=models.DateTimeField(verbose_name=b'Event Date'),
        ),
    ]

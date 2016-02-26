# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='publish_date',
            new_name='date_published',
        ),
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(default=b'Anonymous', max_length=200),
        ),
        migrations.AddField(
            model_name='blog',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2016, 2, 23, 14, 34, 38, 946000, tzinfo=utc), verbose_name=b'Created Date'),
            preserve_default=False,
        ),
    ]

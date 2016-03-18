# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('sec_title', models.CharField(default=b'Give secondary title', max_length=500)),
                ('author', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=500)),
                ('body', models.TextField()),
                ('date_published', models.DateTimeField(verbose_name=b'Date Published')),
                ('created_date', models.DateTimeField(verbose_name=b'Created Date')),
                ('image', models.ImageField(upload_to=b'media/%Y/%m/%d/', blank=True)),
                ('image_title', models.CharField(unique=True, max_length=20)),
            ],
        ),
    ]

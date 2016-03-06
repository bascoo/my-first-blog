# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=1000)),
                ('link', models.CharField(max_length=500)),
                ('date_event', models.DateTimeField(verbose_name=b'Event Date')),
                ('image', models.ImageField(upload_to=b'media/%Y/%m/%d/', blank=True)),
                ('image_title', models.CharField(unique=True, max_length=20, blank=True)),
            ],
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('publish_date', models.DateTimeField(verbose_name=b'Date Published')),
                ('gPlus', models.IntegerField()),
            ],
        ),
    ]

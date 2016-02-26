# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160223_1534'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=250)),
                ('author', models.CharField(default=b'Anonymous', max_length=200)),
                ('body', models.TextField()),
                ('date_published', models.DateTimeField(verbose_name=b'Date Published')),
                ('created_date', models.DateTimeField(verbose_name=b'Created Date')),
                ('gPlus', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]

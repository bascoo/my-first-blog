# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20160223_1545'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='gPlus',
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=200),
        ),
    ]

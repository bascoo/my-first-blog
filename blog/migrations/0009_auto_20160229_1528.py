# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160229_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image_title',
            field=models.CharField(unique=True, max_length=20),
        ),
    ]

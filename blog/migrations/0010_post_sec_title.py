# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160229_1528'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='sec_title',
            field=models.CharField(default=b'Give secondary title', max_length=250),
        ),
    ]

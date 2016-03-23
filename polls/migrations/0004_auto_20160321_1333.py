# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_auto_20160319_1339'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='question_title',
            field=models.CharField(default='Petition', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='question',
            name='question_text',
            field=models.TextField(),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('petition_title', models.CharField(max_length=100)),
                ('petition_text', models.TextField()),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
    ]

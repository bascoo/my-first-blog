# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petition', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('votes', models.IntegerField(default=0)),
                ('vote_title', models.CharField(max_length=10)),
                ('petition', models.ForeignKey(to='petition.Petition')),
            ],
        ),
    ]

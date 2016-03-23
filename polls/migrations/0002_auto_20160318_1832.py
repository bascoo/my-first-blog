# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('petition_title', models.CharField(max_length=200)),
                ('petition_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name=b'date published')),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
        migrations.RemoveField(
            model_name='choise',
            name='question',
        ),
        migrations.DeleteModel(
            name='Choise',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]

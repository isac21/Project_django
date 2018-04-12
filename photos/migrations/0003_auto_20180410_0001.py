# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_auto_20180408_2237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='content',
            field=models.TextField(blank=True, null=True, max_length=500),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('donators', '0002_auto_20150721_2102'),
    ]

    operations = [
        migrations.AddField(
            model_name='donator',
            name='registered',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 18, 5, 21, 572246, tzinfo=utc), auto_now_add=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donator',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 7, 21, 18, 5, 29, 788103, tzinfo=utc), auto_now=True),
            preserve_default=False,
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donator',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('address', models.TextField()),
                ('slug', models.SlugField(unique=True)),
                ('blood_type', models.CharField(default=b'A+', max_length=4, choices=[(b'A+', b'A+'), (b'A-', b'A-'), (b'B+', b'B+'), (b'B-', b'B-'), (b'AB+', b'AB+'), (b'AB-', b'AB-'), (b'0+', b'O+'), (b'0-', b'O-')])),
            ],
        ),
    ]

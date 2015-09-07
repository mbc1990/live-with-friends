# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_auto_20150531_2158'),
    ]

    operations = [
        migrations.AlterField(
            model_name='house',
            name='address',
            field=models.ForeignKey(to='expenses.Address', null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='members',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AlterField(
            model_name='house',
            name='notes',
            field=models.CharField(max_length=200, null=True),
        ),
    ]

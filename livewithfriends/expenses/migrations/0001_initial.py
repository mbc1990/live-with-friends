# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('number', models.IntegerField()),
                ('street', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=200)),
                ('state', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('purchase_date', models.DateTimeField(verbose_name=b'date purchase')),
                ('amount', models.DecimalField(max_digits=7, decimal_places=2)),
                ('payment_method', models.CharField(default=b'De', max_length=2, choices=[(b'Ca', b'Cash'), (b'Cr', b'Credit'), (b'De', b'Debit'), (b'Ch', b'Check')])),
                ('notes', models.CharField(max_length=400)),
                ('creator', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('phone_number', models.IntegerField()),
                ('notes', models.CharField(max_length=400)),
                ('address', models.ForeignKey(to='expenses.Address')),
            ],
        ),
        migrations.AddField(
            model_name='expense',
            name='store',
            field=models.ForeignKey(to='expenses.Store'),
        ),
    ]

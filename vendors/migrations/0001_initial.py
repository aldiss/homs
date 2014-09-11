# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ProductType',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20, verbose_name='\u0412\u0438\u0434 \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=500)),
                ('email', models.EmailField(max_length=75, verbose_name=b'e-mail', blank=True)),
                ('producttype', models.ManyToManyField(to='vendors.ProductType', verbose_name='\u0412\u0438\u0434\u044b \u043f\u0440\u043e\u0434\u0443\u043a\u0446\u0438\u0438')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('description', models.CharField(max_length=500, verbose_name='\u0418\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f \u043e \u0437\u0430\u043a\u0430\u0437\u0435')),
                ('address', models.CharField(max_length=500, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('email', models.EmailField(max_length=75, verbose_name=b'e-mail', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ordernum', models.CharField(max_length=10, verbose_name='\u041d\u043e\u043c\u0435\u0440 \u0437\u0430\u043a\u0430\u0437\u0430')),
                ('date', models.DateField(verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430')),
                ('amount', models.DecimalField(verbose_name='\u0414\u0430\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u0430', max_digits=8, decimal_places=2)),
                ('customer', models.ForeignKey(verbose_name='\u041f\u043e\u043a\u0443\u043f\u0430\u0442\u0435\u043b\u044c', to='customers.Customer')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

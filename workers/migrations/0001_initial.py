# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Worker',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=30, verbose_name='\u0424\u0430\u043c\u0438\u043b\u0438\u044f \u0418\u043c\u044f \u041e\u0442\u0447\u0435\u0441\u0442\u0432\u043e')),
                ('description', models.CharField(max_length=500, verbose_name='\u0414\u043e\u043f\u043e\u043b\u043d\u0438\u0442\u0435\u043b\u044c\u043d\u0430\u044f \u0438\u043d\u0444\u043e\u0440\u043c\u0430\u0446\u0438\u044f')),
                ('daypay', models.DecimalField(verbose_name='\u0421\u0442\u0430\u0432\u043a\u0430 \u0437\u0430 \u0434\u0435\u043d\u044c', max_digits=4, decimal_places=0)),
                ('percentage', models.DecimalField(verbose_name='\u041f\u0440\u043e\u0446\u0435\u043d\u0442 \u043e\u0442 \u043f\u0440\u043e\u0434\u0430\u0436', max_digits=2, decimal_places=1)),
                ('email', models.EmailField(max_length=75, verbose_name=b'e-mail', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]

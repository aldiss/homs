# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workers', '0001_initial'),
        ('vendors', '0003_auto_20140914_0715'),
        ('customers', '0002_auto_20140914_0715'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='cost',
            field=models.DecimalField(null=True, verbose_name='\u0421\u0435\u0431\u0435\u0441\u0442\u043e\u0438\u043c\u043e\u0441\u0442\u044c \u0437\u0430\u043a\u0430\u0437\u0430', max_digits=8, decimal_places=2),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='shipdate',
            field=models.DateField(null=True, verbose_name='\u0414\u0430\u0442\u0430 \u043e\u0442\u0433\u0440\u0443\u0437\u043a\u0438 \u0437\u0430\u043a\u0430\u0437\u0430'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='vendor',
            field=models.ForeignKey(verbose_name='\u041f\u043e\u0441\u0442\u0430\u0432\u0449\u0438\u043a \u043f\u043e \u0437\u0430\u043a\u0430\u0437\u0443', to='vendors.Vendor', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='order',
            name='worker',
            field=models.ForeignKey(verbose_name='\u0414\u0438\u0437\u0430\u0439\u043d\u0435\u0440 \u043f\u043e \u0437\u0430\u043a\u0430\u0437\u0443', to='workers.Worker', null=True),
            preserve_default=True,
        ),
    ]

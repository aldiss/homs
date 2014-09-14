# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendors', '0002_auto_20140913_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='contact',
            field=models.CharField(default=b'contact person', max_length=50, verbose_name='\u041a\u043e\u043d\u0442\u0430\u043a\u0442\u043d\u043e\u0435 \u043b\u0438\u0446\u043e'),
        ),
    ]

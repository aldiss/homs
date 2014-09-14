#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models



class Worker(models.Model):
    name = models.CharField(u"Фамилия Имя Отчество", max_length=30)
    # todo посмотреть какие могут быть шаблоны для ФИО

    description = models.CharField(u"Дополнительная информация", max_length=500)
    daypay = models.DecimalField(u"Ставка за день", max_digits=4, decimal_places=0)
    percentage = models.DecimalField(u"Процент от продаж", max_digits=2, decimal_places=1)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return self.name

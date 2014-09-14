#! /usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models

class ProductType(models.Model):
    name = models.CharField(u"Вид продукции", max_length=20)

    def __unicode__(self):
        return self.name


class Vendor(models.Model):
    name = models.CharField(u"Наименование", max_length=30)
    description = models.CharField(u"Описание", max_length=500)
    producttype = models.ManyToManyField(ProductType, verbose_name=u"Виды продукции")
    email = models.EmailField(blank=True, verbose_name='e-mail')
    contact = models.CharField(u"Контактное лицо", default = 'contact person', max_length=50)

    def __unicode__(self):
        return self.name

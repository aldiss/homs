#! /usr/bin/env python
# -*- coding: utf-8 -*-


from django.db import models




class Customer(models.Model):
    name = models.CharField(u"Фамилия Имя Отчество", max_length=30)
    # todo посмотреть какие могут быть шаблоны для ФИО

    description = models.CharField(u"Информация о заказе", max_length=500)
    address = models.CharField(u"Адрес", max_length=500)
    email = models.EmailField(blank=True, verbose_name='e-mail')

    def __unicode__(self):
        return self.name

class Order(models.Model):
    ordernum = models.CharField(u"Номер заказа", max_length=10)
    # нельзя сделать чисто числовым полем
    customer = models.ForeignKey(Customer, verbose_name=u"Покупатель")
    date = models.DateField(u"Дата заказа")
    shipdate = models.DateField(u"Дата отгрузки заказа", null=True)
    amount = models.DecimalField(u"Сумма заказа", max_digits=8, decimal_places=2)
    cost = models.DecimalField(u"Себестоимость", max_digits=8, decimal_places=2, null=True)
    vendor = models.ForeignKey('vendors.Vendor', verbose_name=u"Поставщик по заказу", null=True)
    # продумать, как можно реализовать двух поставщиков по одному клиентскому заказу.
    # видимо, единственный вариант, это плодить отдельный заказ поставщика
    # и связывать его с Заказом клиента
    worker = models.ForeignKey('workers.Worker', verbose_name=u"Дизайнер по заказу", null=True)



    def __unicode__(self):
        return self.ordernum

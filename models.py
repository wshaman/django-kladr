# -*- coding: utf-8 -*-
from django.db import models

# регионы(области, АО,...)
class Region(models.Model):
    code = models.CharField(u'Код РЕГИОНА', max_length=13, unique=True)
    name = models.CharField(u'Название', max_length=40)
    socr = models.CharField(u'Сокращение', max_length=10)
    index = models.CharField(u'Индекс', max_length=6)
    gninmb = models.CharField(u'ГНИНМБ', max_length=4)
    ocatd = models.CharField(u'ОКАТД', max_length=11, blank=True, null=True)
    uno = models.CharField(u'УНО', max_length=4, blank=True, null=True)
    status = models.CharField(u'Статус', max_length=1)


    def __str__(self):
        return '%s %s'%(self.name, self.socr)

# районы областей
class District(models.Model):
    code = models.CharField(u'Код района', max_length=13, unique=True)
    name = models.CharField(u'Название', max_length=40)
    socr = models.CharField(u'Сокращение', max_length=10)
    index = models.CharField(u'Индекс', max_length=6)
    gninmb = models.CharField(u'ГНИНМБ', max_length=4)
    ocatd = models.CharField(u'ОКАТД', max_length=11, blank=True, null=True)
    uno = models.CharField(u'УНО', max_length=4, blank=True, null=True)
    status = models.CharField(u'Статус', max_length=1)
#    region = models.ForeignKey(Region, to_field='code', verbose_name=u'Регион')
    def __str__(self):
        return '%s %s'%(self.name, self.socr)

# города
class City(models.Model):
    """
    @todo: Есть в КЛАДРЕ особенность, когда в городах есть посёлки, или что-то типа того.

    """
    code = models.CharField(u'Код города', max_length=13, unique=True)
    name = models.CharField(u'Название', max_length=40)
    socr = models.CharField(u'Сокращение', max_length=10)
    index = models.CharField(u'Индекс', max_length=6)
    gninmb = models.CharField(u'ГНИНМБ', max_length=4)
    ocatd = models.CharField(u'ОКАТД', max_length=11, blank=True, null=True)
    uno = models.CharField(u'УНО', max_length=4, blank=True, null=True)
    status = models.CharField(u'Статус', max_length=1)
#    region = models.ForeignKey(Region, to_field='code', verbose_name=u'Регион', blank=True, null=True)
#    district = models.ForeignKey(District, to_field='code', verbose_name=u'Район', blank=True, null=True)
    def __str__(self):
        return '%s %s'%(self.socr, self.name)

#(нас.пункты)
class Ville(models.Model):
    code = models.CharField(u'Код населённого пункта', max_length=13, unique=True)
    name = models.CharField(u'Название', max_length=40)
    socr = models.CharField(u'Сокращение', max_length=10)
    index = models.CharField(u'Индекс', max_length=6)
    gninmb = models.CharField(u'ГНИНМБ', max_length=4)
    ocatd = models.CharField(u'ОКАТД', max_length=11, blank=True, null=True)
    uno = models.CharField(u'УНО', max_length=4, blank=True, null=True)
    status = models.CharField(u'Статус', max_length=1)
#    region = models.ForeignKey(Region, to_field='code', verbose_name=u'Регион', blank=True, null=True)
#    district = models.ForeignKey(District, to_field='code', verbose_name=u'Район', blank=True, null=True)
#    city = models.ForeignKey(City, to_field='code', verbose_name=u'Город', blank=True, null=True)
    def __str__(self):
        return '%s %s'%(self.socr, self.name)

#улицы
class Street(models.Model):
    code = models.CharField(u'Код улицы', max_length=19, unique=True)
    name = models.CharField(u'Название', max_length=40)
    socr = models.CharField(u'Сокращение', max_length=10)
    index = models.CharField(u'Индекс', max_length=6)
    gninmb = models.CharField(u'ГНИНМБ', max_length=4)
    ocatd = models.CharField(u'ОКАТД', max_length=11, blank=True, null=True)
    uno = models.CharField(u'УНО', max_length=4, blank=True, null=True)
#    status = models.CharField(u'Статус', max_length=1)
#    region = models.ForeignKey(Region, to_field='code', verbose_name=u'Регион', blank=True, null=True)
#    district = models.ForeignKey(District, to_field='code', verbose_name=u'Район', blank=True, null=True)
#    city = models.ForeignKey(City, to_field='code', verbose_name=u'Город', blank=True, null=True)
#    ville = models.ForeignKey(Ville, to_field='code', verbose_name=u'Нас. пункт', blank=True, null=True)
    def __str__(self):
        return '%s %s'%(self.socr, self.name)

#дома
class House(models.Model):
    code = models.CharField(u'Код дома', max_length=23, unique=True)
    name = models.CharField(u'Название', max_length=40)
    corp = models.CharField(u'Корпус', max_length=10)
    index = models.CharField(u'Индекс', max_length=6, blank=True, null=True)
    gninmb = models.CharField(u'ГНИНМБ', max_length=4, blank=True, null=True)
    ocatd = models.CharField(u'ОКАТД', max_length=11, blank=True, null=True)
    uno = models.CharField(u'УНО', max_length=4, blank=True, null=True)
#    status = models.CharField(u'Статус', max_length=1)
#    region = models.ForeignKey(Region, to_field='code', verbose_name=u'Регион', blank=True, null=True)
#    district = models.ForeignKey(District, to_field='code', verbose_name=u'Район', blank=True, null=True)
#    city = models.ForeignKey(City, to_field='code', verbose_name=u'Город', blank=True, null=True)
#    ville = models.ForeignKey(Ville, to_field='code', verbose_name=u'Нас. пункт', blank=True, null=True)
#    street = models.ForeignKey(Street, to_field='code', verbose_name=u'Улица', blank=True, null=True)
    def __str__(self):
        return '%s'%(self.name)

#Изменённые названия
class Altnames(models.Model):
    """
    @todo: Выпилить этот ужас!
    """
    old = models.CharField(u'Старый код', max_length=23)
    new = models.CharField(u'Новый код', max_length=23)

#сокращения
class Reductions(models.Model):
    """
    Есть ли в них вообще смысл? пусть остаётся текстом в таблицах
    """
    shortname = models.CharField(u'Сокращение', max_length=10)
    fullname = models.CharField(u'Полное', max_length=29)
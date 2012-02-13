# -*- coding: utf-8 -*-
from django.db.models import Q
from kladr.models import *
import logging


log = logging.getLogger(__name__)

def singleton(cls):
    instances = {}
    def getinstance():
        if cls not in instances:
            instances[cls] = cls()
        return instances[cls]
    return getinstance

@singleton
class Kladdress():
    """
    Класс для работы с КЛАДРом
    @author: serge <serge@shtripling.com>

    @todo: альтернативыне имена
    """
    #Значения типов соответствуют описанию КЛАДРа
    types={ 'region': 1,
            'district': 2,
            'city': 3,
            'ville': 4,
            'street': 5,
            'house': 6,
            'undef': -1
    }
    def _get_class(self, type):
        classes = {
            self.types['region']: Region,
            self.types['district']: District,
            self.types['city']: City,
            self.types['ville']: Ville,
            self.types['street']: Street,
            self.types['house']: House
        }
        try:
            return classes[type]
        except (KeyError, IndexError):
            return None

    def _level_offset(self,lvl):
        o = [0, 0, 2, 5, 8, 11, 15]
        try:
            return o[lvl]
        except IndexError:
            log.error(u'requested wrong KLADR level')
        return 0

    def _seek_altname(self,code):
        return code

    def _get_code_by_lvl(self,code,lvl,strip_zeros=False):
        offset = self._level_offset(lvl+1)
        strip_zeros = 0 if strip_zeros else 1
        return u'%s%s' % (code[:offset],'0'*(len(code)-offset)*strip_zeros)

    def _get_children_code_mask(self, code, lvl=None):
        """Формирует маску для поиска кода объектов нижнего уровня для code
        @todo: учёт статуса и альтернативных имён
        """
        if not lvl:
            lvl = self._calc_level(code)
        offset = self._level_offset(lvl + 1) #маскировать будем детей
        return u'%s%s' % (code[:offset],'')#'0'*(len(code)-offset))

    def _check_if_nzeros(self,s):
        try:
            i = int(s)
        except ValueError:
            return False
        else:
            return i != 0

    def _calc_level(self, code=None ):
        if not code:
            return self.types['undef']
        ## @todo раскурить что за фигня с кодом дома/улицы
        if self._check_if_nzeros(code[14:17]): return self.types['street']#self.types['house']
        if self._check_if_nzeros(code[11:14]): return self.types['street']
        if self._check_if_nzeros(code[8:11]): return self.types['ville']
        if self._check_if_nzeros(code[5:8]): return self.types['city']
        if self._check_if_nzeros(code[2:5]): return self.types['district']
        return self.types['region']

    def get_list(self, parent=None, name_starts=''):
        """
        Получает список объектов
        @param parent string - код вышестоящего объекта.
        @return list
        """
        lvl = self._calc_level(parent)
        if not parent:
            p_level = 1 #детишки
        else:
            p_level = lvl + 1

        r = []
        if parent:
            #Ищем, не устаревший ли код.
            if parent[-2:] != '00':
                parent = self._seek_altname(parent)
            list = self._get_class(p_level).objects.filter(
                Q(code__startswith=self._get_children_code_mask(parent)),
                Q(name__istartswith=name_starts)
                )
            [r.append(x) for x in list]
            if lvl in (self.types['region'], self.types['district'], self.types['city']): # на уровне района ищем и города, и посёлки.
                list=self._get_class(p_level+1).objects.filter(
                    Q(code__startswith=self._get_children_code_mask(parent)),
                    Q(code__startswith=self._get_children_code_mask(parent, p_level)),#избегаем включения через уровень.
                    Q(name__istartswith=name_starts)
                )
                [r.append(x) for x in list]

        else:
            list = self._get_class(p_level).objects.filter(Q(name__istartswith=name_starts) )
            [r.append(x) for x in list]
            if lvl in (self.types['region'], self.types['district'], self.types['city']):
                #list.append(classes[p_level+1].objects.all())
                list = self._get_class(p_level+1).objects.filter(Q(name__istartswith=name_starts) )
                [r.append(x) for x in list]
        return r

    def get_name(self, code=None):
        """
        Получает полное название геграфического объекта
        """
        if not code:
            return ''
        lvl = self._calc_level(code)
        
        o_class = self._get_class(lvl)
        try:
            obj = o_class.objects.get(code=code)
        except o_class.DoesNotExist:
            log.warn(u'%s code requested not found')
            return code

        r = []
        c = []
        for t_ in range(lvl-1):
            t_lvl = t_ + 1
            t_code = self._get_code_by_lvl(code, t_lvl, True)
            t_class = self._get_class(t_lvl)
            try:
                t_obj = t_class.objects.get(code__startswith=t_code)
            except t_class.DoesNotExist:
                pass
            else:
                r.append(t_obj.__str__()) #u'{} {},'.format(r, t_obj)
                c.append(t_obj.code)
#        r = u'{} {}'.format(r, obj)
        r.append(obj.__str__())
        r = {'name':', '.join(r), 'codes': c}
        return r

    def get_codes_by_name(self, name, level=None, parent=None):
        results = []
        if name==u'Азовский':
            name= u'Азовский немецкий национальный'
        try:
            if not parent:
                if level:
                    t = self._get_class(level)
                    results = t.objects.filter(name=name).all()
                else:
                    for i in self.types:
                        if self.types[i]<0 : continue
                        t = self._get_class(self.types[i]).objects.filter(name__istartswith=name).all()
                        [results.append(e) for e in t]
            else:
                l = self.get_list(parent)
                for i in l:
                    if i.name==name:
                        results.append(i)
        except AttributeError:
            pass
        return results

#from kladr.kladdress import Kladdress; o = Kladdress().get_list('5500000000000')

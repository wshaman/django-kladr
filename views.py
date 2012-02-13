# -*- coding: utf-8 -*-

from kladr.kladdress import Kladdress
from main.web_responses import *
#import constants as cs
from django.forms.models import model_to_dict
import logging

log = logging.getLogger(__name__)

def index(request, target=None):
    a_handlers = {
        'getRegions': get_list,
        'getList': get_list,
        'getName': get_name,
        'getPathCodes': get_path_codes,
    }
    try:
        res = a_handlers[target](request)
    except KeyError:
        res = ret_error('WRONG ACTION {}'.format(target))
    return res

def get_list(request):
    code = request.REQUEST.get('code')
    if not request.REQUEST.get('full'):
        fields = ('code', 'name')
    else:
        fields = None
    d = Kladdress().get_list(code,request.REQUEST.get('query', ''))
    data = [model_to_dict(x) for x in d]
    if fields:
        for k,data_item in enumerate(data):
            item = {}
            try:
                for x in fields: item[x] = data_item[x]
            except (KeyError, IndexError):
                log.error('wrong field requested: %s' % field)
            data[k] = item
    return ret_plain(data)

def get_name(request):
    code = request.REQUEST.get('code')
    d = Kladdress().get_name(code)['name']
    return ret_plain(d)

def get_path_codes(request):
    code = request.REQUEST.get('code')
    d = Kladdress().get_name(code)['codes']
    return ret_plain(d)

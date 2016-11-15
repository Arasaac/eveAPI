# coding: utf-8

from eve import Eve
from eve.methods.post import post_internal
from eve.methods.patch import patch_internal
from eve.methods.common import get_document
import json
import os

app = Eve()


def get_id(response):
    return response[0].get('_id').__str__()

DATA = '../utils/'

data = json.load(open( DATA + 'all_data.json'))

def get_id(response):
    return response[0].get('_id').__str__()

def data_to_payload(data):
    '''imagen, id_tipo_imagen, fecha_creacion, ultima_modificacion, autor, web_autor,
    licencia, traduccion, definicion_traduccion'''
    url_videos = 'http://arasaac.org/repositorio/LSE_acepciones/'
    url_images ='http://arasaac.org/repositorio/originales/'
    d = {}
    if data.get('id_tipo_imagen') == 11:
        d['url'] = url_videos + data.get('imagen')
    else:
        d['url'] = url_images + data.get('imagen')
    d['author'] = {}
    d['author']['name'] = data.get('autor')
    if data.get('web_autor'):
        d['author']['web'] = data.get('web_autor')
    d['counter'] = 0
    d['license'] = data.get('licencia')
    d['names'] = []
    name = {'downloads' : 0, 'keyword' : data.get('traduccion')}
    meaning = data.get('definicion_traduccion')
    if meaning:
        name['meaning'] = meaning
    d['names'].append(name)
    d['type'] = data.get('tipo_imagen_en')
    return d

def get_names(data):
    ''' Not used now '''
    name = {'downloads' : 0, 'keyword' : data.get('traduccion')}
    meaning = data.get('definicion_traduccion')
    if meaning:
        name['meaning'] = meaning
    return name

keys_im = {}
with app.test_request_context():
    for d in data:
        payload = data_to_payload(d)
        url = payload.get('url')
        if url in keys_im:
            original = get_document('images', concurrency_check=False, **{'url':url})
            original['names'].extend(payload.get('names'))
            response = patch_internal('images', {'names':original['names']}, **{'url':url})
            if response[-1] == 201 or response[-1] == 200:
                #print ('modificado ',  url)
                pass
            else:
                print ('Error modif.-> ', response, url )
        else:
            response = post_internal('images', payload)
            if response[-1] == 201:
                #print ('añadido ',  url)
                keys_im[url] = get_id(response)
            else:
                print ('Error -> ', response, url )

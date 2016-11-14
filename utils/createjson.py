# coding: utf-8

import MySQLdb
import re
import json

from dbcredentials import *
#DB_USER & DB_PASS

DB_HOST = 'localhost'
DB_NAME = 'arasaac'

con = MySQLdb.connect(host=DB_HOST, user=DB_USER, passwd=DB_PASS, db=DB_NAME, charset='latin1')
cur = con.cursor()


def separa_campos(texto):
    '''Devuelve lista de tags. Están separados por {} en la bd
    '''
    try:
        return [c.strip() for c in re.findall('{(.*?)}', texto) if c.strip()]
    except:
        print (texto)
        return []


sqlen = '''SELECT imagenes.imagen, GROUP_CONCAT(traducciones.traduccion)
FROM imagenes,palabras, palabra_imagen, traducciones WHERE
imagenes.id_imagen = palabra_imagen.id_imagen AND
palabra_imagen.id_palabra = palabras.id_palabra AND
palabras.id_palabra = traducciones.id_palabra AND
traducciones.id_idioma = '7'
GROUP BY imagenes.imagen'''


sqles = '''SELECT imagenes.imagen as imagen, GROUP_CONCAT(palabras.palabra) as palabras, 
imagenes.tags_imagen as tags
FROM imagenes,palabras, palabra_imagen WHERE
imagenes.id_imagen = palabra_imagen.id_imagen AND
palabra_imagen.id_palabra = palabras.id_palabra
GROUP BY imagenes.imagen'''



cur.execute(sqles)
ims = {}

for im, kw, tags in cur.fetchall():
    d = {'url': im}
    d['name'] = dict([('es', [dict([('keyword', k)]) for k in kw.split(',')])])
    if tags:
        _tags = separa_campos(tags.encode('latin1').decode('utf-8'))
        if _tags:
            d['tags'] = dict([('es', _tags)])
    ims[im] = d


cur.execute(sqlen)

for im, kw in cur.fetchall():
    if kw:
        ims[im]['name']['en'] = [dict([('keyword', k)]) for k in kw.split(',')]

con.close()

json.dump(ims.values(), open('lista_imagenes.json', 'w'))

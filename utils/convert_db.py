import MySQLdb
import csv
import collections
#import pypandoc
import re
import json
import datetime

# configure
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASS = 'morico'
DB_NAME = 'arasaac'
connection_data = [DB_HOST, DB_USER, DB_PASS, DB_NAME]
conn = MySQLdb.connect(*connection_data)
cur = conn.cursor()

def table_to_csv(table):
    cur.execute('select * from ' +  table)
    f = open('csvs/' + table+ '.csv', 'w')
    fw = csv.writer(f)
    fw.writerow([r[0] for r in cur.description])
    fw.writerows(cur.fetchall())
    f.close()

def convert_all_db():
    cur.execute('show tables')
    tables = [t[0] for t in cur.fetchall() ]
    for table in tables:
        print  (table)
        table_to_csv(table)


def launch_sql(cursor, query, params=None, fields=None):
    cursor.execute(query, params or [])
    if not fields:
        fields = [col[0] for col in cursor.description]
    row = collections.namedtuple('row', fields)
    for values in cursor.fetchall():
        yield row(*values)

'''
s = sql(cur, "select * from materiales")
ss = [x for x in s]
'''
#import json
#json.dump(ss, open('materiales.json', 'w'))

"""
pypandoc.convert(x, 'plain', format='html')

import re
t = '{4}{5}'
re.findall('{(.*?)}', t)
tt = '{Categorias_Tiendas.doc}{Categorias_Tiendas.pdf}'
re.findall('{(.*?)}', tt)
tt = '{Categorias_Tiendas.doc}   {Categorias_Tiendas.pdf}'
re.findall('{(.*?)}', tt)

'{"material_nivel": "{1}{2}{6}{7}{8}", "material_descripcion": "<p>Fichas de asociaci&oacute;n de distintas profesiones con las acciones y herramientas que las representan.</p><p>Contiene:</p><ul><li>16 l&aacute;minas de asociaci&oacute;n</li><li>1 l&aacute;mina con los nombres de las distintas profesiones</li><li>1 l&aacute;mina modelo</li></ul>", "material_objetivos": "Asociaci\\u00f3n de distintas profesiones con las acciones y herramientas que las respresentan.", "material_archivos": "{Asociacion_Profesiones.zip}", "fecha_alta": "2009-06-13T13:17:25", "material_tipo": "{15}{6}", "material_licencia": 2, "material_area_curricular": "{1}{4}{8}", "material_dirigido": "{1}{11}{12}{5}", "material_subarea_curricular": "{15}{17}", "material_autor": "{4}{5}", "id_material": 1, "material_idiomas": "{es}", "material_titulo": "Fichas de Asociaci\\u00f3n Profesiones - Herramientas", "material_estado": 1, "material_saa": "{12}", "material_edad": "{2}{3}{4}{8}"}'


"""
def separa_campos(texto):
    try:
        return [c.strip() for c in re.findall('{(.*?)}', texto) if c.strip()]
    except:
        print (texto)
        return []

def html_a_texto(texto):
    return pypandoc.convert(texto, 'plain', format='html', encoding='latin-1')

def tabla_materiales():
    cur.execute('select * from materiales')
    materiales = []

    campos = [r[0] for r in cur.description]

    campos_multiples = ["material_nivel", "material_archivos", "material_tipo", "material_area_curricular", "material_dirigido",  "material_subarea_curricular", "material_autor", "material_idiomas", "material_saa", "material_edad"]

    campos_texto = ["material_descripcion", "material_objetivos"]

    for material in cur.fetchall():
        d = dict(zip(campos, material))

        d['fecha_alta'] = d['fecha_alta'].isoformat()

        for campo in campos_multiples:
            d[campo] = separa_campos(d[campo])

        for campo in campos_texto:
            d[campo] = html_a_texto(d[campo])

        materiales.append(d)

    return materiales

def tabla_licencias():
    sql = "select  id_licencia, licencia from licencias"
    return launch_sql( cur, sql, fields=['id', 'name'])

def licencias_json():
    lics = tabla_licencias()
    return json.dumps([li._asdict() for li in lics], default=date_handler)

def tabla_autores():
    sql = "select  id_autor, autor, email_autor from autores"
    return launch_sql( cur, sql, fields=['id', 'name', 'email'] )

def autores_json():
    ims = tabla_autores()
    return json.dumps([im._asdict() for im in ims], default=date_handler)


def tabla_edad():
    cur.execute("select  id_edad_material, edad_material from material_edad")
    edad = []
    for a in cur.fetchall():
        d = {}
        d['id'] = 'e' + str(a[0])
        d['label'] = a[1]
        d['type'] = 'edad'
        edad.append(d)
    return edad

def tabla_nivel():
    cur.execute("select  id_nivel_material, nivel_material from material_nivel")
    nivel = []
    for a in cur.fetchall():
        d = {}
        d['id'] = 'n' + str(a[0])
        d['label'] = a[1]
        d['type'] = 'nivel'
        nivel.append(d)
    return nivel

def tabla_tipo():
    cur.execute("select  id_tipo_material, tipo_material from material_tipo")
    tipo = []
    for a in cur.fetchall():
        d = {}
        d['id'] = 't' + str(a[0])
        d['label'] = a[1]
        d['type'] = 'tipo'
        tipo.append(d)
    return tipo


def date_handler(obj):
    if hasattr(obj, 'isoformat'):
        return obj.isoformat()
    else:
        raise TypeError

def imagenes():
    #sql = "select id_imagen, imagen, id_tipo_imagen, id_licencia, tags_imagen from  imagenes"
    sql = "select id_imagen, imagen, id_tipo_imagen, id_licencia, id_autor from  imagenes"
    return launch_sql(cur, sql, fields=['id', 'path', 'type', 'licence',  'author'])

def imagenes_json():
    ims = imagenes()
    return json.dumps([im._asdict() for im in ims], default=date_handler)

def tags_imagenes():
    sql = "select id_imagen,  tags_imagen from  imagenes"
    cur.execute(sql)

    lista_tags = {}
    for t in cur.fetchall():

        idt = t[0]
        tags = separa_campos(t[1])
        for tag in tags:
            if tag not in lista_tags:
                lista_tags[tag] = [idt]
            else:
                lista_tags[tag].append(idt)

    keys = 'label im'.split()
    lista = [dict(zip(keys, l)) for l in lista_tags]
    json.dump({'items':lista}, open('lista_tags.json', 'w'), encoding='latin1')


def palabras_subtemas():
    sql = ""

def json_to_csv(json_data, f):
    for j in json_data:
        continue

def tipos_imagenes():
    sql = "select id_tipo, tipo_imagen_es  from tipos_imagen"
    return launch_sql(cur, sql, fields=['id', 'name'])

def tipos_json():
    ims = tipos_imagenes()
    return json.dumps([im._asdict() for im in ims], default=date_handler)

def palabras():
    sql = """select palabras.id_palabra, palabra, id_imagen from palabras, palabra_imagen
    where palabras.id_palabra = palabra_imagen.id_palabra
    """
    # sql1 = """select  id_palabra, palabra from palabras"""
    # sql2 = """select  id_palabra, id_imagen  from palabra_imagen"""
    # sql3 = 'select id_palabra, id_subtema from palabra_subtema'

    return launch_sql(cur, sql, fields=['id', 'word', 'im'])

def palabras_json():
    pals = palabras()
    return json.dumps([pal._asdict() for pal in pals], default=date_handler)


def categorias():
    sql1 = "select id_tema, tema from temas"
    sql2 = "select id_tema, id_subtema, subtema from subtemas"

    cur.execute(sql1)
    tes = [t for t in cur.fetchall()]

    cur.execute(sql2)
    subtes = [t for t in cur.fetchall()]

    k = 'id label type'.split()
    dtes = [dict(zip(k, ['c'+str(l[0]), l[1], 'cat'])) for l in tes]

    k = 'id label st type'.split()
    dtes2 = [dict(zip(k, ['c'+str(l[1]), l[2], 'cc'+str(l[0]), 'cat'])) for l in subtes]
    dtes.extend(dtes2)
    return dtes





if __name__ == '__main__':
    '''
    lic = licencias_json()
    open('licences.json', 'w').write(lic)

    ims = imagenes_json()
    open('images.json', 'w').write(ims)

    tims = tipos_json()
    open('timages.json', 'w').write(tims)
    '''
    pals = palabras_json()
    open('palabras.json', 'w').write(pals)




'''
Imagenes no en palabras: {72, 1648, 1649, 1668, 2010, 2118}


run convert_db.py
    sql1 = "select id_tema, tema from temas"
    sql2 = "select id_tema, id_subtema, subtema from subtemas"
cur.execute(slq1)
    sql1 = "select id_tema, tema from temas"
cur.execute(sql1)
tes = [t for t in cur.fetchall()]
cur.execute(sql2)
subtes = [t for t in cur.fetchall()]
len(subtes)
subtes
%hist
tes
k = 'id label type'.split()
dtes = [dict(zip(k, ['c'+str(l[0]), l[0], 'cat'])) for l in tes]
dtes[0]
k = 'label st type'.split()
k = 'id label st type'.split()
dtes[0]
k = 'id label type'.split()
dtes = [dict(zip(k, ['c'+str(l[0]), l[1], 'cat'])) for l in tes]
dtes[0]
k = 'id label st type'.split()
dtes2 = [dict(zip(k, ['c'+str(l[1]), l[2], 'cc'+str(l[0]), 'cat'])) for l in tes]
dtes2 = [dict(zip(k, ['c'+str(l[1]), l[2], 'cc'+str(l[0]), 'cat'])) for l in tes2]
dtes2 = [dict(zip(k, ['c'+str(l[1]), l[2], 'cc'+str(l[0]), 'cat'])) for l in subtes]
dtes2
k = 'id label st type'.split()
dtes = [dict(zip(k, ['cc'+str(l[0]), l[1], 'cat'])) for l in tes]
len(dtes)
dtes.extend(dtes2)
len(dtes)
dtes
json
json.dump({'items':dtes}, open('catalogo.json', 'w'))


'''


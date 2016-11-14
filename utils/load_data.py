from eve import Eve
from eve.methods.post import post_internal
import json
import os

SETTINGS_PATH = '../app'

os.chdir(SETTINGS_PATH)

app = Eve()

def get_id(response):
    return response[0].get('_id').__str__()

DATA = '../utils/'


authors = json.load(open(DATA + 'authors.json'))

keys_auth = {}
with app.test_request_context():
    for payload in authors:
        k = payload.pop('id')
        if not payload.get('email'):
            payload.pop('email')
        response = post_internal('authors', payload)
        if response[-1] == 201:
            keys_auth[k] = get_id(response)
        else:
            print ('Error -> ', response[-1], k )
            break

json.dump(keys_auth, open(DATA + 'authors_keys.json', 'w'))


# Load Images
images = json.load(open(DATA + 'images.json'))
timages = json.load(open(DATA + 'timages.json'))
licences = json.load(open(DATA + 'licences.json'))

tim = {} # dicc imágenes
for t in timages:
    tim[t.get('id')] = t.get('name')

lic = {}
for li in licences:
    lic[li.get('id')] = li.get('name')

keys_im = {}
with app.test_request_context():
    for payload in images:
        k = payload.pop('id')
        if payload['author'] == 1:
            payload['author'] = 2
        payload['license'] = lic[payload.pop('licence')]
        payload['url'] = payload.pop('path')
        payload['author'] = keys_auth[payload['author']]
        payload['type'] = tim.get(payload['type'])

        response = post_internal('images', payload)
        if response[-1] == 201:
            keys_im[k] = get_id(response)
        else:
            print ('Error -> ', response[-1], k )
            break
json.dump(keys_im, open('ims_keys.json', 'w'))


# Load Words
words = json.load(open(DATA + 'palabras_dict.json')).values()

with app.test_request_context():
    for payload in words:
        images = payload.pop('ims')
        payload['images'] = [keys_im[i] for i in images]
        k = payload.pop('id')
        payload['lang'] = 'es'
        response = post_internal('words', payload)
        if response[-1] == 201:
            pass
        else:
            print ('Error -> ', response[-1], k )
            break

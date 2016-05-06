from eve import Eve
from eve.methods.post import post_internal
import json

ims = json.load(open('lista_imagenes.json'))

app = Eve()

with app.test_request_context():
	for n, payload in enumerate(ims):
	    x = post_internal('images', payload)
	    print(n)

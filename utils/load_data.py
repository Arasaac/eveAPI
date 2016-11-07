from eve import Eve
from eve.methods.post import post_internal
import json

ims = json.load(open('authors.json'))

app = Eve()

with app.test_request_context():
    for n, payload in enumerate(ims):
        del(payload['id'])
        if n < 1:
            x = post_internal('authors', payload)
            print(x)

from eve import Eve
from eve_swagger import swagger, add_documentation

import os

SETTINGS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.py')

app = Eve(settings=SETTINGS_PATH)

# swagger config
app.register_blueprint(swagger)
app.config['SWAGGER_INFO'] = {
    'title': 'Arasaac new API',
    'version': '0.1',
    'description': 'New API for accesing pictograms and material',
    'termsOfService': 'TODO',
    'contact': {
        'name': 'Arasaac Team',
        'url': 'https://github.com/arasaac'
    },
    'license': {
        'name': 'CC by SA',
        'url': 'https://github.com/arasaac',
    }
}

# optional. Will use flask.request.host if missing.
# app.config['SWAGGER_HOST'] = 'myhost.com'

# optional. Add/Update elements in the documentation at run-time without deleting subtrees.
'''
add_documentation({'paths': {'/images': {'get': {'parameters': [
    {
        'in': 'query',
        'name': 'foobar',
        'required': False,
        'description': 'special query parameter',
        'type': 'string'
    }]
}}}})
'''

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

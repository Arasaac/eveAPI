# coding: utf-8

'''
test_juanda = {
    "image": 1234,
    "name": {
        "es": [
            {"keyword": "comida",
            "locution": 34567,
            "meaning": "Acto de alimentarse a mediodía",
            "lse": 17589,
            "type": "noun",
            "downloads": 0 },
            {"keyword": "cena", "locution": 23657, "meaning": "Acto de alimentarse por la noche", "lse": 17629, "type": "noun", "downloads": 0}
            ],
        "en": [
            {"keyword": "lunch", "locution": 34569, "meaning": "Act of eating food at noon", "type": "noun", "downloads": 0 },
            {"keyword": "dinner", "locution": 23657, "meaning": "Act of eating food in the afternon", "type": "noun", "downloads": 0 }
       ]
    },
    "status": "publish",
    "type":  "pictogram",
    "creacionDate": ISODate("1927-09-04T04:00:00Z"),
    "license": "MIT",
    "author":
        [{"name": "Pepito", "surname": "González",  "email": "prueba@prueba.com", "url": "http://www.marca.es", "company": "DGA"}],

    "tags": {
      "es": [{"keyword": "alimentos", "downloads": 0}],
            "en": [{"keyword": "food", "downloads": 0}]
    },
    "size": ["small", "medium", "big"],
    "url": "http://www.myweb.com/images/1234.jpg"
    }


schema = {
    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'name': {
        'type': 'dict',
        'schema': { 'valueschema': {'type': 'list'}
            'address': {'type': 'string'},
            'city': {'type': 'string'}
        },
    },
    'lastname': {
        'type':

'''

required_string = {
    'type': 'string',
    'required': True,
    'empty': False
}

string = {'type': 'string'}

objectid = {'type': 'string'}

doc = {
    "url": '1234.jpg',
    "name": {
        "es": [
            {"keyword": "comida",
            "locution": '34567',
            "meaning": "Acto de alimentarse a mediodía",
            "lse": '17589',
            "type": "noun",
            },
            {"keyword": "cena", "locution": '23657', "meaning": "Acto de alimentarse por la noche", "lse": '17629', "type": "noun"}
            ],
        'en': [
            {"keyword": "lunch", "locution": '34569', "meaning": "Act of eating food at noon", "type": "noun"},
            {"keyword": "dinner", "locution": '23657', "meaning": "Act of eating food in the afternon", "type": "noun"}
       ]
    },
    "status": "publish",
    "type":  "pictogram",
    "creationDate": "1927-09-04T04:00:00Z",
    "license": "MIT",
    "author":
        [{"name": "Pepito",
        "surname": "González",
        "email": "prueba@prueba.com",
        "url": "http://www.marca.es",
        "company": "DGA"}],

    "tags": {
      "es": ["alimentos", "verduras", "jamancia"],
      "en": ["food"]
        },
    }


_i18n_name = {
    'type': 'dict',
    'schema': {
        'keyword': required_string,
        'locution': objectid,
        'meaning': string,
        'lse': objectid,
        'type': string
        }
    }

_name = {
    'type': 'dict',
    'propertyschema': {'type': 'string'},
    'valueschema': {'type': 'list',
                    'schema': _i18n_name}
    }

_author = {
    'type': 'dict',
    'schema': {
        'name': string,
        'surname': string,
        'email': string,
        'url': string,
        'company': string
        }
}

_authors = {
    'type': 'list',
    'schema': _author}

_tags = {
    'type': 'dict',
    'propertyschema': {'type': 'string'},
    'valueschema': {'type': 'list', 'schema': string}
    }

schema_images = {
    'url': string,
    'name': _name,
    'status': string,
    'license': string,
    'type': string,
    'creationDate': {'type': 'string'},  # datetime !
    'author' : _authors,
    'tags' : _tags
    }


if __name__ == '__main__':

    # from cerberus import Validator
    from eve.io.mongo import Validator

    v = Validator(schema_images)
    # v.allow_unknown = True
    v.validate(doc)

    print(v.errors)

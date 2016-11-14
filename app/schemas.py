schema_images = {
    'schema': {
        'creationDate': {
            'type': 'string'
        },
        'modificationDate': {
            'type': 'string'
        },
        'url': {
            'type': 'string'
        },
        'author': {
            'type': 'objectid',
            'data_relation': {
                'resource': 'authors',
                'field': '_id',
                'embeddable': True
            }
        },
        'counter': {
            'type': 'integer'
        },
        'license': {
            'type': 'string'
        },
        'type': {
            'type': 'string'
        }
    }
}

schema_authors = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'email': {
            'type': 'string',
            'required': False,
            'nullable': True
        }
    }
}

schema_words = {
    'schema': {
        'word': {
            'type': 'string'
        },
        'lang': {
            'type': 'string'
        },
        'images': {
            'type': 'list',
            'schema': {
                'type': 'objectid',
                'data_relation': {
                    'resource': 'images',
                    'field': '_id',
                    'embeddable': True
                }
            }
        },
        'type': {
            'type': 'string',
            'required': False,
            'nullable': True

        },
        'categories': {
            'type': 'list',
            'schema': {
                'type': 'string'
            },
            'required': False,
            'nullable': True
        }
    }
}

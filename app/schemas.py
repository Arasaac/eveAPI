schema_images = {
    'schema': {
        'author': {
            'schema': {
                'name': {
                    'type': 'string'
                },
                'web': {
                    'type': 'string'
                }
            },
            'type': 'dict'
        },
        'counter': {
            'type': 'integer'
        },
        'creationDate': {
            'type': 'string'
        },
        'license': {
            'type': 'string'
        },
        'modificationDate': {
            'type': 'string'
        },
        'names': {
            'schema': {
                'schema': {
                    'downloads': {
                        'type': 'integer'
                    },
                    'keyword': {
                        'type': 'string'
                    },
                    'locution': {
                        'type': 'string'
                    },
                    'meaning': {
                        'type': 'string'
                    },
                    'sl': {
                        'type': 'string'
                    },
                    'type': {
                        'type': 'string'
                    },
                },
                'type': 'dict'
            },
            'type': 'list'
        },

        'tags': {
            'schema': {
                'schema': {
                    'downloads': {
                        'type': 'integer'
                    },
                    'keyword': {
                        'type': 'string'
                    },
                },
                'type': 'dict'
            },
            'type': 'list'
        },
        'type': {
            'type': 'string'
        },
        'url': {
            'type': 'string'
        }
    }
}
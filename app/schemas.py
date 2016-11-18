schema_images = {
    'schema': {
        'author': {
            'schema': {
                'name': {
                    'type': 'string',
                    'description': 'Name of the author'
                },
                'web': {
                    'type': 'string',
                    'description': 'Web of the author'
                }
            },
            'type': 'dict'
        },
        'counter': {
            'type': 'integer',
            'description': 'number of times accessed (for improving the searches)'
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
            'description': 'list of names of the image',
            'schema': {
                'schema': {
                    'downloads': {
                        'type': 'integer',
                        'description': 'number of times downloaded using this name',
                    },
                    'keyword': {
                        'type': 'string',
                        'description': 'name'
                    },
                    'locution': {
                        'type': 'string',
                        'description': 'url of the locution (sound)'
                    },
                    'meaning': {
                        'type': 'string',
                        'description': 'descriptive meaning'
                    },
                    'sl': {
                        'type': 'string',
                        'description': 'video in sing language'
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

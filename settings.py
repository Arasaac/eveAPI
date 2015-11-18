# Let's just use the local mongod instance. Edit as needed.

# Please note that MONGO_HOST and MONGO_PORT could very well be left
# out as they already default to a bare bones local 'mongod' instance.
#

import os

MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
MONGO_PORT = os.environ.get('MONGO_PORT', 27017)
# MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
# MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'user')
MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'arasaac')


RESOURCE_METHODS = ['GET']
ITEM_METHODS = ['GET']

schema_image = {
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'name': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 250,
        'required': True,
    },
    # 'role' is a list, and can only contain values from 'allowed'.

}


images = {
    # 'title' tag used in item links.
    'item_title': 'image',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'path'
    },

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'path': {
            'type': 'string',
            'minlength': 1,
            'maxlength': 250,
            'required': True,
            'unique': True,
         },
        'license': {
            'type': 'list',
            'required': True,
        },
        # 'role' is a list, and can only contain values from 'allowed'.
        'type': {
            'type': 'objectid',
        }
        },
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
}

catalog = {
    # 'title' tag used in item links.
    'item_title': 'catalog',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>/'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform GET
    # requests at '/people/<lastname>/'.

    # Schema definition, based on Cerberus grammar. Check the Cerberus project
    # (https://github.com/nicolaiarocci/cerberus) for details.
    'schema': {
        'label': {
            'type': 'dict',
            'required': True,
         },
        'subtopicof': {
            'type': 'objectid',
        },
        },
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
}



DOMAIN = {
    'images': images,
    'catalog':  catalog,

}

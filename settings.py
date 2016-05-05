# coding: utf-8

MONGO_HOST = 'localhost'
MONGO_PORT = 27017
MONGO_DBNAME = 'arasaactest'

# Enable reads (GET), inserts (POST) and DELETE for resources/collections
# (if you omit this line, the API will default to ['GET'] and provide
# read-only access to the endpoint).
# RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
RESOURCE_METHODS = ['GET']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
#ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
ITEM_METHODS = ['GET']

from schema import schema_images

images = {
    'item_title': 'image',
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
    'resource_methods': ['GET'],
    'schema': schema_images
}


DOMAIN = {'images': images, 'materials': {}, 'lse': {}}

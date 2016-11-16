# coding: utf-8
import os

if os.environ.get('TESTING') is None:
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
    MONGO_USERNAME = os.environ.get('MONGO_USERNAME', 'user')
    MONGO_PASSWORD = os.environ.get('MONGO_PASSWORD', 'pw')
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'arasaac2')
else:
    MONGO_HOST = os.environ.get('MONGO_HOST', 'localhost')
    MONGO_PORT = int(os.environ.get('MONGO_PORT', 27017))
    MONGO_DBNAME = os.environ.get('MONGO_DBNAME', 'arasaac2')

# $PORT is defined if we are hosted on Heroku
if os.environ.get('PORT') is None:
    DEBUG = True

#MONGO_HOST = 'mongo'
MONGO_HOST = 'localhost'
MONGO_PORT = 27017
# MONGO_USERNAME = 'user'
# MONGO_PASSWORD = 'user'
MONGO_DBNAME = MONGO_DBNAME

# RESOURCE_METHODS = ['GET', 'POST', 'DELETE']
RESOURCE_METHODS = ['GET']

# Enable reads (GET), edits (PATCH), replacements (PUT) and deletes of
# individual items  (defaults to read-only item access).
#ITEM_METHODS = ['GET', 'PATCH', 'PUT', 'DELETE']
ITEM_METHODS = ['GET']

from schemas import schema_images

images = {
    # 'title' tag used in item links. Defaults to the resource title minus
    # the final, plural 's' (works fine in most cases but not for 'people')
    'item_title': 'image',

    # by default the standard item entry point is defined as
    # '/people/<ObjectId>'. We leave it untouched, and we also enable an
    # additional read-only entry point. This way consumers can also perform
    # GET requests at '/people/<lastname>'.
    #'additional_lookup': {
    #    'url': 'regex("[\w]+")',
    #    'field': 'lastname'
    #},

    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,

    # most global settings can be overridden at resource level
    'resource_methods': ['GET'],

    'schema': schema_images.get('schema')
}

DOMAIN = {'images': images}

X_DOMAINS = "*"

URL_PREFIX = 'api'
#API_VERSION = 'v1'

# Accept-Language request headers
LANGUAGE_DEFAULT = 'en'
LANGUAGES = {
    'en': 'English',
    'es': 'Español',
    'fr': 'French',
    'pt': 'Portuguese',
    'ar': 'Arabic'
}


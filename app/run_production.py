
# -*- coding: utf-8 -*-
"""
    arasaac_api.run_production.py
    ~~~~~~~~~~~~~~~~~~~~~~
    Production script sample, using Tornado.
    :copyright: (c) 2016 by @lmorillas
    :license: BSD, see LICENSE for more details.
"""

from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from eve import Eve

app = Eve()

http_server = HTTPServer(WSGIContainer(app))
http_server.listen(5000)
IOLoop.instance().start()

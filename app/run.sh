#!/usr/bin/env sh
gunicorn -w 4 -b 0:5000 arasaac:app


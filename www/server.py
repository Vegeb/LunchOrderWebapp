# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:03:30 2015

@author: dbi
"""

#server.py
from wsgiref.simple_server import make_server

from hello import application

#create server
httpd = make_server('',8000, application)
print('Serving HTTP on port 8000')

httpd.serve_forever()

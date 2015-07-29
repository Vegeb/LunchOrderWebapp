# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 16:16:07 2015

@author: dbi
"""
def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hi, %s!<h1>' %(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]
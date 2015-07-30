# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 14:44:31 2015

@author: dbi
"""

import re, time, json, logging, hashlib, base64, asyncio

from coroweb import get, post

from models import User, Comment, Blog, next_id

@get('/')
def index(request):
    users = yield from User.findAll()
    return {
        '__template__': 'test.html',
        'users': users
    }
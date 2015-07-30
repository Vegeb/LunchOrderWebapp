# -*- coding: utf-8 -*-
"""
Created on Thu Jul 30 11:45:08 2015

@author: dbi
"""
import orm,asyncio
from models import User,Blog,Comment

def test(loop):
    yield from orm.create_pool(loop=loop,user='root',password='password',db='awesome')
    u=User(id='123',name='test2',email='test7@test.com',passwd='test',image='about:blank')
    yield from u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
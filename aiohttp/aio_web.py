#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'Michael Liao'

'''
async web application.
'''
import logging; logging.basicConfig(level=logging.INFO)

import asyncio

from aiohttp import web

async def index(request):
    print("index_in")
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>')
    print("index_out")

async def hello(request):
    print("hello_in")
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=text.encode('utf-8'))
    print("hello_out")

async def init(loop):
    print("init_in")
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    srv = await loop.create_server(app.make_handler(), '127.0.0.1', 8000)
    print('Server started at http://127.0.0.1:8000...')
    logging.info('server started at http://127.0.0.1:8000...')
    return srv
    print("init_out")

print("first")
loop = asyncio.get_event_loop()
print("second")
loop.run_until_complete(init(loop))
print("third")
loop.run_forever()
print("end")
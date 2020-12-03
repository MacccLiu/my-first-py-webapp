# -*- coding: utf-8 -*-
import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime
from aiohttp import web

routes = web.RouteTableDef()
@routes.get('/')
def index(request):
    return web.Response(body=b'<h1>Hello</h1>', content_type='text/html')

async def init():
    app = web.Application()
    app.add_routes(routes)
    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, '127.0.0.1', 9000)
    await site.start()
    print('======= Running on http://127.0.0.1:9000 ========')

loop = asyncio.get_event_loop()
loop.run_until_complete(init())
loop.run_forever()

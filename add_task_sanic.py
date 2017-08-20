# -*- coding: utf-8 -*-

import asyncio 

from sanic import Sanic
from sanic.response import json

app = Sanic()


#@app.listener('before_server_start')
#async def setup_db(app, loop):
#    app.db = await db_setup()

#@app.listener('after_server_start')
#async def notify_server_started(app, loop):
#    print('Server successfully started!')
#
#@app.listener('before_server_stop')
#async def notify_server_stopping(app, loop):
#    print('Server shutting down!')
#
#@app.listener('after_server_stop')
#async def close_db(app, loop):
#    await app.db.close()
#

async def notify_server_started_after_five_seconds():
    await asyncio.sleep(5)
    print('Server successfully started!')

app.add_task(notify_server_started_after_five_seconds())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

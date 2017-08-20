# -*- coding: utf-8 -*-

from sanic import Sanic
#from sanic.response import json

from sanic.response import text

app = Sanic()


#####NOTE: @app.route
#
#@app.route('/get', methods=['GET'], host='example.com')
#async def get_handler(request):
#    return text('GET request - {}'.format(request.args))
#
#
## if the host header doesn't match example.com, this route will be used
#@app.route('/get', methods=['GET'])
#async def get_handler(request):
#    return text('GET request in default - {}'.format(request.args))
#

####NOTE: @app.get, @app.post
@app.post('/post')
async def post_handler(request):
    return text('POST request - {}'.format(request.json))

@app.get('/get')
async def get_handler(request):
    return text('GET request - {}'.format(request.args))


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001)

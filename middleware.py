from sanic import Sanic
from sanic import Blueprint
from sanic.response import json
from sanic.response import text


app = Sanic(__name__)
bp = Blueprint('name', url_prefix='/my_blueprint')


@bp.route('/foo')
async def foo(request):
    return json({'msg': 'hi from blueprint'})



@bp.middleware
async def print_on_request(request):
    print("I am a spy")

@bp.middleware('request')
async def halt_request(request):
    return text('I halted the request')

@bp.middleware('response')
async def halt_response(request, response):
    return text('I halted the response')

app.blueprint(bp)

app.run(host="0.0.0.0", port=8000, debug=True)

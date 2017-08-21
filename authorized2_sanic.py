# -*- coding: utf-8 -*-

from sanic import Sanic
from functools import wraps
from sanic.response import json

app = Sanic()


def check_request_for_authorization_status(request=''):
    # Note: Define your check.
    flag = True
    return flag


def authorized(method):
    """Decorate methods with this to require that the user be logged in.
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        is_authorized = check_request_for_authorization_status()
        if is_authorized:
            return method(self, *args, **kwargs)
        else:
            # the user is not authorized. 
            return json({'status': 'not_authorized'}, 403)
 
        return method(self, *args, **kwargs)
    return wrapper 

@app.route("/")
@authorized  # NOTE: note the difference.
async def test(request):
    return json({'status': 'authorized'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)

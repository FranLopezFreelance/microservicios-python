import json
from wsgiref.simple_server import make_server

def application(environ, start_response):
    headers = [('Content-type', 'application/json')]

    start_response('200 OK', headers)

    response = {
        'message' : 'Hola Mundo desde el Servidor'
    }

    return [ bytes(json.dumps(response), 'utf-8')]

server = make_server('localhost', 7000, application)
server.handle_request()
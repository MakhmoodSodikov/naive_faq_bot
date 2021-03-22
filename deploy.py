from gevent.pywsgi import WSGIServer
from app import app

http_server = WSGIServer(('', 5050), app)
http_server.serve_forever()

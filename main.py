from gevent.pywsgi import WSGIServer
from server import app

WSGIServer(('0.0.0.0', 8000), app).serve_forever()

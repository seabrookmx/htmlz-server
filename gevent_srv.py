import os
from gevent.pywsgi import WSGIServer
from ebook_server import app

PORT = int(os.getenv('HTMLZ_PORT', '5000'))

http_server = WSGIServer(('', PORT), app)
http_server.serve_forever()

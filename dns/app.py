import datetime
from wsgiref.simple_server import WSGIServer
import os
from flask import Flask

from dns.config import *
from dns.routes import *

# APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
# CONFIG_ROOT = os.path.join(APP_ROOT, 'config.py')   # caminho para o ficheiro confyg.py

app = Flask(__name__)

# Regista o endpoint dnsRoute
app.register_blueprint(dnsRoute)


# Aviso no IP 127.0.0.1
@app.route("/")
def index():
    return "Computação Distribuida : BlockChain DNS" + ' {0:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())


if __name__ == '__main__':
    if SERVER_MODE_DEV:
        app.run(host='0.0.0.0', port=SERVER_PORT, debug=True)
    else:
        http_server = WSGIServer(('', SERVER_PORT), app)
        http_server.serve_forever()

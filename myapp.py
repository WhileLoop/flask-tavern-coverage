import signal

from flask import Flask, jsonify
from flask import request

def create_app():
    app = Flask(__name__)

    @app.route('/ping')
    def ping():
        return jsonify(ping = 'pong')

    return app

if __name__ == '__main__': # pragma: no cover
    app = create_app()
    app.run(port = 8080)

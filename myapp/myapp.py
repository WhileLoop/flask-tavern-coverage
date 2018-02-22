from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/ping')
def ping():
    return jsonify(ping = 'pong')


@app.route('/double')
def double():
    number = request.args.get('number')
    return jsonify(double = int(number) * 2)


if __name__ == '__main__':
    app.run(port = 8080)

from flask import Flask
from flask import request, json, Response, jsonify

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Hello World'

@app.route('/hello', methods = ['GET'])
def api_hello():
    data = {
        'message': 'Konnichiwa',
        'result': 'success'
    }
    resp = jsonify(data)
    resp.status_code = 200

    return resp

@app.route('/users/<user_id>', methods = ['GET'])
def api_users(user_id):
    users = {'1': 'sakura', '2': 'hanazawa', '3': 'Akano'}

    if user_id in users:
        return jsonify({'user': users[user_id]})
    else:
        return not_found()

@app.route('/messages', methods = ['POST'])
def api_message():

    if request.headers['Content-Type'] == 'text/plain':
        return "Text Message: " + request.data

    elif request.headers['Content-Type'] == 'application/json':
        return "JSON Message: " + json.dumps(request.json)

    elif request.headers['Content-Type'] == 'application/octet-stream':
        f = open('./binary', 'wb')
        f.write(request.data)
        f.close()
        return "Binary message written!"

    else:
        return "415 Unsupported Media Type :("

@app.errorhandler(404)
def not_found():
    message = {
        'status': 404,
        'message': 'Not found: ' + request.url
    }
    resp = jsonify(message)
    resp.status_code = 404

    return resp


if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import request

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Hello World'

@app.route('/hello')
def api_hello():
    if 'name' in request.args:
        return 'Hello ' + request.args['name']
    else:
        return 'Hello'

if __name__ == '__main__':
    app.run(debug=True)

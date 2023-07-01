from flask import Flask
from flask_socketio import SocketIO, emit


app = Flask(__name__)
socketio = SocketIO(app)

# Define event handler for 'message' event
@socketio.on('message')
def handleMessage(msg):
    print(f'Message: {msg}')
    emit('message', msg, broadcast=True)

@app.route('/')
def index():
    return "Working"


if __name__ == '__main__':
    socketio.run(app, debug=True)
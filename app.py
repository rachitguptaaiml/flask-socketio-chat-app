import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key_here'
socketio = SocketIO(app)

@socketio.on('connect')
def handle_connect():
    print('Client connected')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

@socketio.on('message')
def handle_message(data):
    message = f'Client {data["client_id"]} said: {data["message"]}'
    emit('message', {'text': message}, broadcast=True)

if __name__ == '__main__':
    socketio.run(app, host='localhost', port=5000)
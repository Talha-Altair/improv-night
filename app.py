from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit , send
import random

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/',methods=['GET']) 
def home():
    return render_template('secret.html')

@app.route('/404') 
def home2():
    return render_template('404.html')

@app.route('/events',methods=['GET']) 
def home3():
    name = request.values.get("name")
    print(name)
    more_lines = [' ',name]

    with open('static/player.txt', 'a') as f:
        f.writelines('\n'.join(more_lines))

    return render_template('events.html')

@app.route('/players',methods=['GET','POST']) 
def home4():
    names = ""
    with open('static/player.txt') as f:
        contents = f.readlines()

    name_dict = {
        "names" : contents
    }
    
    return jsonify(name_dict)



@socketio.on('message')
def message():
    events = [
        'Elevator Pitching','Ship-Wreck','Quiz-Game','fan-Fiction'
        ]
    n = random.randint(0,4)
    event = events[n]
    socketio.emit('completed',event)

if __name__ == "__main__":
    socketio.run(app, debug = True)

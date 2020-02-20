import datetime
from flask import Flask
app = Flask(__name__)


@app.route('/time')
def hello_world():
    time = datetime.datetime.now()
    return 'Hello world, time is \t' + str(time)


app.run(host='0.0.0.0',port=8080,debug=True)

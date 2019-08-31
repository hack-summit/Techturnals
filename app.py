
from flask import Flask
import simplejson as json 

app=Flask(__name__)

@app.route('/')
def index():
    return 'Server works!!'


@app.route('/greet')
def say_hello():
  return 'Hello from Server'


@app.route('/api/attendance/<id>',methods = ['POST'])
def attendanceD(id):
  print(id)
  data={
    'hey':'killer',
    'happy':'yup',
    'id':id
  }
  
  return json.dumps(data) 











from flask import Flask
import simplejson as json 
from flask import request
import sqlite3  


app=Flask(__name__)

def select(query):
  db=s.connect('hospital.db')
  cur=db.cursor()
  val=cur.execute(query)
  db.close()
  return val

def update(query):
  db=s.connect('hospital.db')
  cur=db.cursor()
  val=cur.execute(query)
  db.commit()
  db.close()
  return val



@app.route('/')
def index():
    return 'Server works!!'


@app.route('/greet')
def say_hello():
  return 'Hello from Server'


@app.route('/api/attendance/<id>',methods = ['POST','GET'])
def attendanceD(id):
  print(id)
  data={
    'hey':'killer',
    'happy':'yup',
    'id':id
  }

  return json.dumps(data) 

@app.route('/login',methods=['POST'])
def loginDN():
  k=request.args
  g=request.form
  f=request.data
  t=request.values
  h=request.headers
  usr = request.headers['username']
  pwd = request.headers['password']
  print(h)
  print(k)
  print(g)
  print(f)
  print(t)
  print('Social values:',usr,pwd)
  ret='Hellow'+str(usr)+pwd
  hash(f)

  return ret









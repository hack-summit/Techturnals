
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

def select_dict(query):
  result = select(query)
  column_names = []
  return_list = []
  for row in result.description:
    column_names.append(row[0])
  result = result.fetchall()
  for res in xrange(len(result)):
    temp_dict = {}
    for col in xrange(len(column_names)):
      temp_dict.update({column_names[col]:result[res][col]})
      return_list.append(temp_dict)
      dict1 = {'result':return_list}
  return dict1

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

def getRand(n):
  return 'g'*n
@app.route('/login',methods=['POST'])
def loginDN():
  usr = request.headers['username']
  pwd = request.headers['password']
  
  ret={}

  arr=select('select password from doctor where UserName=\''+usr+'\'')
  arr2=select('select password from Nurse where UserName=\''+usr+'\'')
  validate='12345678'
  doc=False
  done=False
  fo=0
  for i1 in arr:
    if(str(i1)==str(pwd)):
      validate=getRand(8)
      ret['token']=validate
      ret['Post']='Doctor'
      update('update table "Doctor" set LastLogin=now(), LoginToken=\''+validate+'\' where UserName=\''+usr+'\' ')
      done=True
      doc=True
      break

  if(not done):
    done=False
    for i1 in arr2:
      if(str(i1)==str(pwd)):
          validate=getRand(8)
      ret['token']=validate
      ret['Post']='Nurse'
      update('update table "Nurse" set LastLogin=now(), LoginToken=\''+validate+'\' where UserName=\''+usr+'\' ')
      done=True
      break
  ret['token']=validate

  if (done and doc):
    v=select('select id from doctor where UserName=\''+usr+'\'')
    for i in v:
      fo=i
  elif(done and not doc):
    v=select('select id from nurse where UserName=\''+usr+'\'')
    for i in v:
      fo=i
  nur={}
  val=select_dict('select DateIn (select id from "Nurse" where DoctorID='+fo+')')
  return json.dumps(ret)









"""
  k=request.args
  g=request.form
  f=request.data
  t=request.values
  h=request.headers
  usr = request.headers['username']
  pwd = request.headers['password']
  print('Social values:',usr,pwd)
  ret='Hellow'+str(usr)+pwd
  ret=ret+str(hash(f))
  """
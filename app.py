from flask import Flask
from flask import render_template
import os

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/xhr/<req>')
def xhr(req):
   print req
   f1=open('abc.java','w')
   f1.write(req)
   f1.close()
   os.system("javac abc.java")
   os.system("java abc > result.txt")

   f2=open('result.txt','r')
   lines=f2.readlines()
   f2.close()
   new=""
   for L in lines:
    	new=new+L
   return new

@app.route('/home')
def home():
    return render_template('Client.html')

if __name__ == '__main__':
    app.run(debug='true')

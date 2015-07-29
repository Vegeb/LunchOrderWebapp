# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 17:25:32 2015

@author: dbi
"""

from flask import Flask
from flask import request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])

def home():
    return render_template('home.html')
    
@app.route('/signin', methods=['GET'])

def sigin_form():
    return render_template('form.html')



@app.route('/signin', methods=['POST'])
def signin():
    username = request.form['username']
    password = request.form['password']
    if username=='admin' and password=='password':
        return render_template('signin-ok.html', username=username)
    return render_template('form.html', message='Bad username or password', username=username)


if __name__ == '__main__':
    app.run()
    
from flask import Flask, render_template, request, redirect, session, flash, make_response
from datetime import datetime
from mysqlconnection import connectToMySQL    # import the function that will return an instance of a connection
import secrets
app = Flask(__name__)

app.config["SECRET_KEY"] = secrets.token_urlsafe(16)

@app.route('/')
def index():
  if 'key' in session.keys() and session['keys'] != None:
    return redirect('/dashbaord')
  return redirect('/main')


@app.route('/register', methods=["POST"])
def register():
  is_valid = True
  for i in key_list:
    if i not in request.form.keys():
      is_valid = False
      flash('All fields required!')
  if len(request.form['username']) < 2 or len(request.form['name']) < 2:
    is_valid = False
    flash('Name and Username needs to be at least 3 characters.')
  if request.form['password'] and request.form['confirm_pw']:
    if request.form['password'] != request.form['confirm_pw']:
      is_valid = False
      flash('Passwords do not match.')
    elif request.form['password'] == request.form['confirm_pw'] and len(request.form['password']) < 7:
      is_valid = False
      flash('Password must be at least 8 characters.')
  if request.form['username']:
    mysql = connectToMySQL('task_board')
    user_query = next((item for item in mysql.query_db("SELECT * FROM *") if item["username"] == request.form['username']), None)
    if user_query:
      if request.form['username'] == user_query['username']:
        is_valid = False
        flash('Username already in use. Please login or use another username.')
  if is_valid == False:
    return redirect('/main')
  else:
    flash('Account created! Please login.')
    mysql = connectToMySQL("task_board")
    query = mysql.query_db("INSERT INTO users (name, username, password, date_hired) VALUES ('%s', '%s', '%s', '%s');" % (request.form['name'], request.form['username'], request.form['password'], request.form['date_hired']))
    return redirect('/dashboard')


@app.route('/login', methods=["POST"])
def login():
  is_valid = True
  if request.form['username']:
    mysql = connectToMySQL('task_board')
    user_query = next((item for item in mysql.query_db("SELECT * FROM users") if item["username"] == request.form["username"]), None)
    if user_query:
      if request.form['username'] == user_query['username']:
        if request.form['password'] == user_query['password']:
          session['user'] = user_query['id']
          session['name'] = user_query['name']
          session['key'] = secrets.token_urlsafe(16)
          return redirect('/dashboard')
        else:
          is_valid = False
      else:
        is_valid = False
    else:
      is_valid = False
  else:
    is_valid = False
    flash('Email or Password is not valid.')
  return redirect('/')


@app.route('/log_out')
def log_out():
  session.clear()
  user_dict = {
    'route': 'home'
  }
  return redirect('/')

if __name__=="__main__":
  app.run(debug=True)
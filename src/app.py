from flask import Flask, render_template, request, flash, g
from flask_bootstrap import Bootstrap
from sqlite3 import connect, Connection
from datetime import datetime
app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'development key'
from forms import ServiceRequestForm, ClientRegistrationForm

DATABASE = '../db/easydoesit.db'

# Returns a SQLite3 Connection Object
def connect_db():
  return connect(DATABASE)

def close_db(connection):
  connection.close()

@app.route("/")
def welcome():
  return "Welcome to the app"

@app.route('/service_request', methods=['GET', 'POST'])
def service_request():
  # THIS NEEDS TO ALL BE SANITIZED!!!!
  if request.method == 'POST':
    db = connect_db()
    if not db:
      return '404'
    sr = {}
    uid = request.form['uid']
    tid = request.form['service_type']
    urg = request.form['urgency']
    loc = request.form['location']
    gen = request.form['gender']
    start_time = str(datetime.now())
    cmd = """INSERT INTO ServiceRequests
             (cid, service_type, address, start_time, emergency_level, 
             gender_pref) VALUES ({}, {}, '{}', '{}', {}, '{}');"""\
             .format(uid, tid, loc, start_time, urg, gen)
    c = db.cursor()
    c.execute(cmd)
    c.execute('select * from ServiceRequests')
    result = c.fetchall()
    db.close()
    return str(result)
  elif request.method == 'GET':
    form = ServiceRequestForm()
    return render_template('service_request.html', form=form)

def main():
  app.run(debug=True)

if __name__ == '__main__':
  main()




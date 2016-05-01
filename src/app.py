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
    tid = request.form['Type']
    loc = request.form['DestinationLocation']
    rsn = request.form['Reason']
    name = request.form['Name']
    gen = request.form['Gender']

    start_time = str(datetime.now())
    c = db.cursor()
    c.execute("select cid from Clients where name = ?;", name)
    uid = c.fetchone()

    c.execute( """INSERT INTO ServiceRequests
             (cid, service_type, address, start_time, emergency_level, 
             gender_pref) VALUES (?, ?, '?', '?', ?, '?');""", (uid, tid, loc, start_time, 2, gen))
    c.execute('select * from ServiceRequests')
    result = c.fetchall()
    db.close()
    return 'Good'
  elif request.method == 'GET':
    form = ServiceRequestForm()
    return render_template('service_request.html', form=form)

def main():
  app.run(debug=True)

if __name__ == '__main__':
  main()




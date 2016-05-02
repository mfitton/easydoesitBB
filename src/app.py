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

def service_type_to_id(service_type):
    """Converts a service type string to an integer service type ID"""
    db = connect_db()
    if not db:
        return '404'
    c = db.cursor()
    c.execute("""SELECT stid FROM Services WHERE type=?""", service_type)
    num = c.fetchone()
    db.close()
    return num

@app.route("/")
def welcome():
  return "Welcome to the app"

@app.route('/dispatch', methods=['GET'])
def dispatch_view():
  db = connect_db()
  if not db:
    return "couldn't find db"
  c = db.cursor()
  # name, time, urgency, phone, gender_pref
  c.execute("""select c.name, sr.start_time, sr.emergency_level, 
                      c.phone_number, sr.gender_pref
                    FROM Clients as c JOIN ServiceRequests sr ON
                      c.cid = sr.cid""")
  service_reqs = c.fetchall()
  return render_template('service_request.html', service_requests=service_requests)


@app.route('/service_request', methods=['GET', 'POST'])
def service_request():
  if request.method == 'POST':
    db = connect_db()
    if not db:
      return '404'
    
    params = request.get_json()
    service_type_string = params['Type']
    tid = service_type_to_id(service_type_string)
    loc = params['DestinationLocation']
    rsn = params['Reason']
    name = params['Name']
    gen = params['Gender']
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
  app.run(host='0.0.0.0')

if __name__ == '__main__':
  main()

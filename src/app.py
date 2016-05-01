from flask import Flask, render_template, request, flash
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)
app.secret_key = 'development key'
from forms import ServiceRequestForm




@app.route("/")
def welcome():
    return "Welcome to the app"

  
@app.route('/service_request', methods=['GET', 'POST'])
def service_request():
  form = ServiceRequestForm()
 
  if request.method == 'POST':
    return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('service_request.html', form=form)


def main():
    app.run(debug=True)

if __name__ == '__main__':
    main()




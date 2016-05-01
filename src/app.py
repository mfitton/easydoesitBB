from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the app"

@app.route("/<name>")
def echo_name(name):
    return "Hello " + name

def main():
    app.run()

if __name__ == '__main__':
    main()


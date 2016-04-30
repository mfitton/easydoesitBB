from flask import Flask
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the app"

def main():
    app.run()

if __name__ == '__main__':
    main()


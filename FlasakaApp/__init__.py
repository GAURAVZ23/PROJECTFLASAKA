from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html", title = "epic website in the making", paragraph = "this is gonna be a party..")

if __name__ == "__main__":
    app.run()


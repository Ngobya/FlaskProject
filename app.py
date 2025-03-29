from flask import Flask, render_template  # import

app = Flask(__name__)  # declaration of your app to respond to requests


@app.route("/")  # Default route
def Home():
    my_title = "Home"
    context = {"my title": my_title}
    return render_template("home.html", **context )

@app.route("/About")  # About route
def About():
    return "<p>About!<p>"

@app.route("/Contact Us")  # Contact route
def Contact():
    return "<p>Contacts!<p>"

@app.route("/Gallery")  # Gallery route
def Gallery():
    return "<p>Gallery!<p>"

if __name__ == "__main__":
    app.run(debug=True)

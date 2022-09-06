from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "count"


@app.route('/')
def index():
    if "count" not in session:
        session["count"] = 1
    else:    
        session["count"] += 1
    
    return render_template("index.html")

@app.route("/increment", methods=["POST"])
def increment_count():
    if request.form["increment"]== "add":
        session["count"] += 1
    elif request.form["increment"]== "reset":
        session["count"] = 0

    return redirect("/")

@app.route("/destroy_session")
def destroy_session():
    session.clear()

    return redirect("/")


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

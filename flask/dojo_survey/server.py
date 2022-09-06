from flask import Flask, render_template, request, redirect, session  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "survey"

@app.route('/')          
def render_form():
    return render_template("index.html")

@app.route('/process', methods=['POST']) 
def process_form():
    print(request.form)
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']

    return redirect("/result")

@app.route('/result')
def show_info():
    return render_template("display.html")

@app.route("/clear")
def clear_session():
    session.clear()
    
    return redirect('/')


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

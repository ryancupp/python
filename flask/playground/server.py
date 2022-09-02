from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"

@app.route('/play')
def Welcome():
    return render_template('index.html') 

@app.route('/play/<int:number>')
def make_box(number):
    return render_template("boxes.html", number=number)

@app.route('/play/<int:number>/<color_change>')
def change_color(number, color_change):
    colorChange = color_change
    return render_template("boxes2.html", number=number, colorChange = color_change)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

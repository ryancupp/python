from flask import Flask, render_template, request, redirect # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
from users import User

@app.route('/')
def index():
    return redirect('/users')


@app.route('/users')
def users():
    return render_template("read_all.html",users=User.get_all())

@app.route('/user/new')
def new():
    return render_template("create_user.html")

@app.route('/user/create',methods=['POST'])
def create():
    print(request.form)
    User.create(request.form)
    return redirect('/users')

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("read_one.html",user=User.get_one(data))

@app.route('/user/edit/<int:id>')
def edit(id):
    data ={ 
        "id":id
    }
    return render_template("edit_user.html",user=User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.edit(request.form)
    return redirect('/users')

@app.route('/user/delete/<int:id>')
def delete(id):
    data ={
        'id': id
    }
    User.delete(data)
    return redirect('/users')




if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.

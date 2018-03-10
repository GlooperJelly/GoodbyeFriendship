from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def index():
    user = {'username' : 'Ben'}
    data = [
        {
            'author':{'username':'Ben'},
            'body':'test post'
        },
        {
            'author':{'username':'Bebo'},
            'body':'Four!'
        }
    ]
    return render_template('index.html', title='home', user = user, posts = data )
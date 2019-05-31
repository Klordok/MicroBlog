from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user  = {'username': 'Mort'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Mesa!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'i hate mondays'
        }
    ]

    return render_template('index.html', title='Homepage', user=user, posts=posts)
from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Ivy'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Nairobi'
        },
        {
            'author': {'username': 'Malik'},
            'body': 'It is very windy'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
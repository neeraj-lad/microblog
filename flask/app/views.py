from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Miguel'} # mock user
    posts =  [   # mock array of posts
            {
                'author': {'nickname': 'John'},
                'body': 'Beautiful day!'
                },
            {
                'author': {'nickname': 'Susan'},
                'body': 'Today I Learned'
                },
            {
                'author': {'nickname': 'James'},
                'body': 'Baaaah..'
                },
            {
                'author': {'nickname': 'Cris'},
                'body': 'Me, me, me!'
                },
            {
                'author': {'nickname': 'Flo'},
                'body': 'Hahahoho'
                }
            ] 
    return render_template('index.html',
                            title='Home',
                            user=user,
                            posts=posts)

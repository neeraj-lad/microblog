from flask import render_template, flash, redirect
from app import app
from .forms import LoginForm

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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for OpenID="%s", remember_me=%s' % (form.openid.data, str(form.remember_me.data)))
        return redirect('/index')
    return render_template('login.html',
                            title='Sign-In',
                            form=form,
                            providers=app.config['OPENID_PROVIDERS'])

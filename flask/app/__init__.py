from flask import Flask

app = Flask(__name__)
app.config.from_object('cfg')

from app import views

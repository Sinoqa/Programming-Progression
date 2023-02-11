from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user

@app.route('/')
def index():
    all_users = user.User.get_all_users()
    return render_template('index.html', users = all_users)

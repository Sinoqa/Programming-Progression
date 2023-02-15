from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, book
from flask_app.controllers import books

@app.route('/')
def index():
    all_users = user.User.get_all_users()
    return render_template('index.html', users = all_users)


@app.route('/users/profile/<id>')
def show_user_profile(id):
    this_user = user.User.get_user_id(id)   
    return render_template('profile.html', user = this_user)


@app.route('/users/update/<id>', methods = ['POST', 'GET'])
def update_user(id):
    if request.method == 'POST':
        user.User.update_user(request.form)
        return redirect('/')
    if request.method == 'GET':
        this_user = user.User.get_user_id(id)
        return render_template ('edit_user.html', user  = this_user)


@app.route('/users/create', methods=['POST', 'GET'])
def create_user():
    if request.method == 'POST':
        user.User.create_user(request.form)
        return redirect('/')
    if request.method =='GET':
        return render_template('create_user.html')

@app.route('/users/delete/<id>')
def delete_user(id):
    user.User.delete_user(id)
    return redirect ('/')


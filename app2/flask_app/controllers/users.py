from flask_app import app
from flask import Flask, redirect, render_template, session, request
from flask_app.models import user


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/shop')
def shop_flowers():
    return render_template('shop.html')

@app.route('/buyers')
def buyers():
    all_buyers = user.User.get_all_buyers()
    return render_template('buyers.html', buyers = all_buyers )

# @app.route('/create_buyer', methods=['POST', 'GET'])
# def method_name(id):
#     # if request.method == 'POST':
#     #     user.User.create_user(request.form)
#     #     return redirect ('/buyers')
#     # if request.method == 'GET':
#         user.User.get_user_by_id(id)
#         return render_template('create_buyer.html')

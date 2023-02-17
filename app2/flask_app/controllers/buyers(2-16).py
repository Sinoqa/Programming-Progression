from flask_app import app
from flask import redirect, render_template, session, request
from flask_app.models import user, flower


@app.route('/')
def homepage():
    return render_template('index.html')


@app.route('/shop')
def shop_flowers():
    all_flowers = flower.Flower.get_all_flowers()
    return render_template('shop.html', flowers = all_flowers)
@app.route('/buyers')
def buyers():
    all_buyers = user.User.get_all_buyers()
    return render_template('buyers.html', buyers = all_buyers )

@app.route('/create_buyer', methods=['POST', 'GET'])
def create_buyer():
    if request.method == 'POST':
        user.User.create_buyer(request.form)
        return redirect ('/buyers')
    if request.method == 'GET':
        return render_template('create_buyer.html')


@app.route('/flowers')
def flower_browse():
    all_flowers = flower.Flower.get_all_flowers()
    return render_template('flowers.html', flowers = all_flowers)

@app.route('/flowers/buy/<id>', methods=['POST', 'GET'])
def method_dname():
    pass
from flask_app import app
from flask import render_template, redirect, request, session, flash
from flask_app.models import user, book


@app.route('')
def method_name():
    pass
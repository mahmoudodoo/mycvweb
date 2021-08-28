from flask import render_template,redirect,request
from app import app

@app.route('/')
def about_me_view():
    return render_template('about_me.html')
from flask import render_template,redirect,request,url_for
from . import main
#from ..request 
#from ..models

@main.route('/')
def index():
    return  render_template('index.html')

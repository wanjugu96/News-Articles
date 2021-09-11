from flask import render_template,redirect,request,url_for
from . import main
from ..request import get_sources
#from ..models

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    sportsources=get_sources('technology')
    print(sportsources)

    return  render_template('index.html',sportsources=sportsources)

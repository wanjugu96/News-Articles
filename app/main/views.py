from flask import render_template,redirect,request,url_for
from . import main
from ..request import get_sources
#from ..models

@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''
    Techsources=get_sources('technology')
    #category=Techsources.category

    sportsources=get_sources('sports')
    businesssources=get_sources('business')
    entertainment=get_sources('entertainment')
    health=get_sources('health')
    
    print(sportsources)

    return  render_template('index.html',health=health,sportsources=sportsources,Techsources=Techsources,businesssources=businesssources,entertainment=entertainment)

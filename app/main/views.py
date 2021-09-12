from flask import render_template,redirect,request,url_for
from . import main
from ..request import get_sources,get_articles
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
    # biz_sources=get_sources('sports')
    
    # for biz_source in biz_sources:
    #     biz_source.id=id

    
    sportsources=get_sources('sports')
    sourceid=sportsources[0].id

    articles=get_articles(sourceid)
  



   
    return  render_template('index.html',sourceid=sourceid,health=health,sportsources=sportsources,Techsources=Techsources,businesssources=businesssources,entertainment=entertainment)

@main.route('/<sourceid>')
def articles(sourceid):
    
   

    sportsources=get_sources('sports')
    sourceid=sportsources[0].id

    #articles=get_articles('wired')
    articles=get_articles(sourceid)




    return render_template('articles.html',articles=articles,sourceid=sourceid)
                            



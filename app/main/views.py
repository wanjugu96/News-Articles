from flask import render_template,redirect,request,url_for
from . import main
from ..request import  get_one_source, get_sources,get_articles,get_source
#from ..models

@main.route('/<sourceid>',methods = ['GET', 'POST'])
def sports_articles(sourceid):
   #sportsources=get_sources('sports')

    # for sportsource in sportsources:
    #     id=sportsource.id
    #     sportssourceid=id
    articles=get_articles(sourceid)

    #articles=get_articles('wired')
    #articles=get_articles(sportssourceid)

    return render_template('articles.html',articles=articles,)


@main.route('/' ,methods = ['GET', 'POST'])

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

    
    sportsources=get_sources('sports')
    if request.method == 'POST':
        sourceid=request.form['sourceid']

        return redirect(url_for('.sports_articles',sourceid=sourceid))

    return render_template('index.html',sources=Techsources)
  
@main.route('/business' ,methods = ['GET', 'POST'])

def business():
    '''
    View root page function that returns the business sources page
    '''
    
    
    businesssources=get_sources('business')
   
    if request.method == 'POST':
        sourceid=request.form['sourceid']

        return redirect(url_for('.sports_articles',sourceid=sourceid))

  
    return  render_template('business.html',sources=businesssources)


    
# @main.route('/')                           
# def business_articles():

#     businesssources=get_sources('sports')
#     articles=get_article_list(businesssources)
#     return render_template('articles.html',articles=articles)
                            


from flask import render_template,redirect,request,url_for
from . import main
from ..request import  get_one_source, get_sources,get_articles,get_source
#from ..models

@main.route('/<sourceid>',methods = ['GET', 'POST'])
def articles(sourceid):
  
    articles=get_articles(sourceid)

    sourcename=sourceid

    return render_template('articles.html',articles=articles,sourcename=sourcename)


@main.route('/' ,methods = ['GET', 'POST'])

def index():
    '''
    View root page function that returns the index page and its data
    '''
    
    Techsources=get_sources('technology')
   
    if request.method == 'POST':
        sourceid=request.form['sourceid']

        return redirect(url_for('.articles',sourceid=sourceid))

    return render_template('index.html',sources=Techsources)
  
@main.route('/business' ,methods = ['GET', 'POST'])

def business():
    '''
    View root page function that returns the business sources page
    '''
    
    
    businesssources=get_sources('business')
   
    if request.method == 'POST':
        sourceid=request.form['sourceid']

        return redirect(url_for('.articles',sourceid=sourceid))

  
    return  render_template('business.html',sources=businesssources)


    
@main.route('/entertainment' ,methods = ['GET', 'POST'])

def entertainment():
    '''
    View root page function that returns the business sources page
    '''
    
    businesssources=get_sources('entertainment')
   
    if request.method == 'POST':
        sourceid=request.form['sourceid']

        return redirect(url_for('.articles',sourceid=sourceid))

  
    return  render_template('entertainment.html',sources=businesssources)

@main.route('/sports' ,methods = ['GET', 'POST'])

def sports():
    '''
    View root page function that returns the business sources page
    '''
    
    sportsources=get_sources('sports')
   
    if request.method == 'POST':
        sourceid=request.form['sourceid']

        return redirect(url_for('.articles',sourceid=sourceid))

  
    return  render_template('sports.html',sources=sportsources)


    
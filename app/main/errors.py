from flask import render_template
from . import main

@main.app_errorhandler(404)
def fourowfour(error):
    '''
    function to render 404 page
    '''
    return render_template('error.html'),404
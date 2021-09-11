import urllib.request,json
from .models import Article,Source

#getting api key and base url

api_key=None
base_url=None

def configure_request(app):
    global articles_base_url,sources_base_url
    api_key=app.config['NEWS_API_KEY']
    articles_base_url=app.config['NEWS_ARTICLES_BASE_URL']
    sources_base_url=app.config['NEWS_SOURCES_BASE_URL']

import urllib.request,json
from .models import Sources

#getting api key and base url

api_key=None
sources_base_url=None

def configure_request(app):
    global articles_base_url,sources_base_url,api_key
    api_key=app.config['NEWS_API_KEY']
    articles_base_url=app.config['NEWS_ARTICLES_BASE_URL']
    sources_base_url=app.config['NEWS_SOURCES_BASE_URL']


def get_sources(category):
    '''
    function that gets all our news sources
    '''

    get_sources_url=sources_base_url.format(category,api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data=url.read()
        get_sources_response=json.loads(get_sources_data)

        sources_results=None

        if get_sources_response['sources']:
            sources_results_list=get_sources_response['sources']
            sources_results=process_results(sources_results_list)

        
    return sources_results

def get_articles(source):
    '''
    function that gets all our news sources
    '''
    get_articles_url=articles_base_url.format(source,api_key)

    with urllib.request.irlopen(get_articles_url)as url:
        get_aricles_data=url.read()
        get_articles_response=json.loads(get_aricles_data)


        articles_results=None

        if get_articles_response['articles']:
            articles_results_list=get_articles_response['articles']
            articles_results=process_results(articles_results_list)
    
    return articles_results




def process_results(sources_list):

    '''
    Function  that processes the movie result and transform them to a list of Objects
    '''
    sources_results=[]
    for source_item in sources_list:
        id=source_item.get('id')
        name=source_item.get('name')
        description=source_item.get('description')
        url=source_item.get('url')
        category=source_item.get('category')
      

        source_obj=Sources(id,name,description,url,category)

        sources_results.append(source_obj)

    return sources_results



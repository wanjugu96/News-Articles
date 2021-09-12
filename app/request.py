import urllib.request,json
from .models import Sources,Article

#getting api key and base url

api_key=None
sources_base_url=None

def configure_request(app):
    global articles_base_url,sources_base_url,api_key
    api_key=app.config['NEWS_API_KEY']
    articles_base_url=app.config['NEWS_ARTICLES_BASE_URL']
    sources_base_url=app.config['NEWS_SOURCES_BASE_URL']

def get_source(source_id,category):
    '''
    function that gets all our news sources
    '''

    get_source_url=sources_base_url.format(category,api_key)

    with urllib.request.urlopen(get_source_url) as url:
        get_source_data=url.read()
        get_source_response=json.loads(get_source_data)

        source_object=None

        if get_source_response:
            id=get_source_response.get('id')
            name=get_source_response.get('name')
            description=get_source_response.get('description')
            url=get_source_response.get('url')
            category=get_source_response.get('category')

            source_object=Sources(id,name,description,url,category)

    return source_object

      
            

        
    # return sources_results
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

    with urllib.request.urlopen(get_articles_url)as url:
        get_aricles_data=url.read()
        get_articles_response=json.loads(get_aricles_data)


        articles_results=None

        if get_articles_response['articles']:
            articles_results_list=get_articles_response['articles']
            articles_results=process_articles(articles_results_list)
    
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


def process_articles(articles_list):

    '''
    Function  that processes the movie result and transform them to a list of Objects
    '''
    article_result=[]
    for article_item in articles_list:
        title=article_item.get('title')
        url=article_item.get('url')
        description=article_item.get('description')
        urlToImage=article_item.get('urlToImage')
        publishedAt=article_item.get('publishedAt')
        source=article_item.get('source')
        author=article_item.get('author')
        article_obj=Article(title,description,url,urlToImage,publishedAt,source,author)

        article_result.append(article_obj)

    return article_result


def get_one_source(id,category):

    sources=get_sources(category)
    for source in sources:
        if source.id==id:
            return source
    
    return source

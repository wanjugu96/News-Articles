import os
class Config:
    NEWS_ARTICLES_BASE_URL='https://newsapi.org/v2/top-headlines?sources={}&apiKey={}'
    NEWS_SOURCES_BASE_URL='https://newsapi.org/v2/top-headlines/sources?category={}&language=en&apiKey={}'

    #https://newsapi.org/v2/top-headlines?sources=bbc-news&apiKey=b7b2a5ee0f444390abfb0b9c2d91502c
    #GET https://newsapi.org/v2/top-headlines?country=de&category=business&apiKey=b7b2a5ee0f444390abfb0b9c2d91502c
#GET https://newsapi.org/v2/top-headlines/sources?category=businessapiKey=API_KEY

    NEWS_API_KEY=os.environ.get('NEWS_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')


class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG=True

config_options={
    'development':DevConfig,
    'production':ProdConfig
}



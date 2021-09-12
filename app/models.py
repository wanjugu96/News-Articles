class Sources:
    '''
    class to define news sources
    '''
    pass

    def __init__(self,id,name,description,url,category):
        self.id=id
        self.name=name
        self.description=description
        self.url=url
        self.category=category

class Article:
    '''
    class to define a news article object
    '''
    def __init__(self,title,description,url,urlToImage,publishedAt,source ,author):
        self.publishedAt=publishedAt
        self.title=title
        self.description=description
        self.url=url
        self.urlToImage=urlToImage
        self.source=source
        self.author=author

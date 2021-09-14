import unittest
from app.models import Article

class ArticleTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the article class
    '''
    def setUp(self):
        '''
        Set up method to run before any tes
        '''

#title,description,url,urlToImage,publishedAt,source ,author
        self.new_article=Article("Dancing stars","who can dance","example.com","exampleimage.com","12-3-3","BBC","Mary")

    def test_instance(self):
        self.assertTrue(isinstance (self.new_article,Article))
        self.assertEqual(self.new_article.title,"Dancing Stars")
        self.assertEqual(self.new_article.description,"who can dance")
        self.assertEqual(self.new_article.url,"example.com")
        self.assertEqual(self.new_article.urlToImage,"exampleimage.com")
        self.assertEqual(self.new_article.publishedAt,"12-3-3")
        self.assertEqual(self.new_article.source,"BBC","Mary")


     



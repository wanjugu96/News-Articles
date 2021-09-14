import unittest
from app.models import Sources
#id,name,description,url,category

class sourcetest(unittest.TestCase):
    '''
    class to test the source class behaviors
    '''
    def setUp(self):

        self.new_source=Sources("bbc","bbc","number1","example.com","category")

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source),Sources)

        self.assertEqual(self.new_source.id,"bbc")
        self.assertEqual(self.new_source.name,"bbc")
        self.assertEqual(self.new_source.description,"number1")
        self.assertEqual(self.new_source.url,"example.com")
        self.assertEqual(self.new_source.category,"category")

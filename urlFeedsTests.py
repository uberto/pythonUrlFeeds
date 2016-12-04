import unittest

from urlFeeds import *
from article import *

def fun(x):
    return x + 1

  

class MyTest(unittest.TestCase):

    def setUp(self):
        self.rssExample = """someResult = {
    'feedEntries': [{
    url: "www.arkera.ai/article/1",
    title: "Article 1, The Story of Arkera’s Beginnings",
    imageUrl: "www.arkera.ai/article/image/1"
    }, {
    url: "www.arkera.ai/article/2",
    title: "Article 2, The Story of Arkera’s Beginnings 2",
    imageUrl: "www.arkera.ai/article/image/2"
    }]
}"""   
 
    def testSuccess(self):
        self.assertEqual(fun(3), 4)

    def testCreateArticles(self):
        a1 = Article(title='article one', html= 'div')
        self.assertEqual(a1.title, 'article one')
        self.assertEqual(a1.html, 'div')


    def testProcessUrlLists(self):
        urls = extractUrlsFromRss(self.rssExample)
        self.assertEqual(len(urls), 2)



if __name__ == '__main__':
    unittest.main()
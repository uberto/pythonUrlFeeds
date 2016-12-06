import unittest
import os
import string

from urlFeeds import *
from article import *
from persistence import *
from workers import *


def fun(x):
    return x + 1

  

class MyTest(unittest.TestCase):


    def setUp(self):
        self.rssExample = """{
    "feedEntries": [{
    "url": "http://wikipedia.org",
    "title": "Article 1, The Story of Arkera’s Beginnings",
    "imageUrl": "www.arkera.ai/article/image/1"
    }, {
    "url": "www.arkera.ai/article/2",
    "title": "Article 2, The Story of Arkera’s Beginnings 2",
    "imageUrl": "www.arkera.ai/article/image/2"
    }]
}"""
        self.db = Persistence('testDb.json')


    def tearDown(self):
        self.db.dropTables()
    
    def testSuccess(self):
        self.assertEqual(fun(3), 4)

    def testCreateArticles(self):
        a1 = Article(title='article one', url= 'div', html="", tags=[])
        self.assertEqual(a1.title, 'article one')
        self.assertEqual(a1.url, 'div')

    def testTagArticle(self):
        a1 = Article(title='article one', url= 'div', html="", tags=[])
        tagged = a1.tagArticle('t1', 't2')
        self.assertEqual(len(tagged.tags), 2)
        self.assertEqual(tagged.tags[0], 't1')
        self.assertEqual(tagged.tags[1], 't2')


    def testProcessUrlLists(self):
        arts = extractUrlsFromJsonRss(self.rssExample)
        self.assertEqual(len(arts), 2)
        self.assertEqual(arts[0].title, 'Article 1, The Story of Arkera’s Beginnings')
        self.assertEqual(arts[1].url, 'www.arkera.ai/article/2')
        self.assertFalse(arts[1].isFetched())


    def testPersistArticles(self):
        a1 = Article(title='article one', url= 'http://', html="", tags=[])
        
        self.db.saveArticle(a1)

        newa1 = self.db.findArticle('article one')

        self.assertEqual(newa1.title, 'article one')
        self.assertEqual(newa1.url, 'http://')

    def testFetchFromUrl(self):
        arts = extractUrlsFromJsonRss(self.rssExample)
        a1 = arts[0].fetchArticleFromUrl()
        print("fetched %d bytes" % len(a1.html))
        self.assertTrue(a1.isFetched())


    def testFetchFromQueue(self):
        l = []
        for a in list(string.ascii_uppercase):
            l.append(Article(title=a, url='http://en.wikipedia.org/wiki/' + a, html='', tags=[]))
        processAndSaveAll(self.db, l)



if __name__ == '__main__':
    unittest.main()
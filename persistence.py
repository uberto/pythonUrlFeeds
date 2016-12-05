from tinydb import TinyDB, Query
from article import *

class Persistence:

    def __init__(self):
        self.articleDb = TinyDB('articleDb.json')
        
    def saveArticle(self, article):
        self.articleDb.insert(article._asdict())

    def findArticle(self, title):
        query = Query()
        results = self.articleDb.search(query.title == title)
        
        print("--------> " + str(len(results)))

        return Article(**results[0]) 
    
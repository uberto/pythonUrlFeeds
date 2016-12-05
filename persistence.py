from tinydb import TinyDB, Query
from article import *

ARTICLES_DB = 'articleDb.json'
class Persistence:

    def __init__(self):
        self.articleDb = TinyDB(ARTICLES_DB)
        
    def saveArticle(self, article):
        self.articleDb.insert(article._asdict())

    def findArticle(self, title):
        query = Query()
        results = self.articleDb.search(query.title == title)

        return Article(**results[0]) 

    def dropTables(self):
        self.articleDb.purge_tables()
        self.articleDb.close()
    
    
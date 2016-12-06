from tinydb import TinyDB, Query
from article import *


class Persistence:

    def __init__(self, fileName):
        self.articleDb = TinyDB(fileName)
        
    def saveArticle(self, article):
        self.articleDb.insert(article._asdict())

    def findArticle(self, title):
        query = Query()
        results = self.articleDb.search(query.title == title)

        return Article(**results[0]) 

    def dropTables(self):
        self.articleDb.purge_tables()
        self.articleDb.close()
    
    
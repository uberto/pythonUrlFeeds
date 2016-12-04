from collections import namedtuple

class Article(namedtuple('Article', 'title html')):

    def isValid(self):
        return True


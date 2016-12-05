from collections import namedtuple

class Article(namedtuple('Article', 'title html url')):

    def isFetched(self):
        return self.html


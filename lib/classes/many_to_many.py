class Article:
    def __init__(self, author, magazine, title):
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    def __init__(self, name):

        if not isinstance(name, str):
            raise valueError("Name must be of type str.")
        if len(name) = 0:
            raise valueError("Name must be longer than 0 characters.")
        self.name = name
        self._articles = []
        self._margazines = []


    def articles(self):
        pass

    def magazines(self):
        pass

    def add_article(self, magazine, title):
        pass

    def topic_areas(self):
        pass

class Magazine:
    def __init__(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def add_article(self, name, category):
        self.name = name
        self.category = category
        self._articles = []

    def add_article(self, article):  #adds article to the magazine 
        self._artcicles.append(article)

    def articles(self)
        return self._articles   #returns a list of articles in the magazine 
        pass
    

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
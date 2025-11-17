class Article:
    all= []
    def __init__(self, author, magazine, title):
        # Validating the title 
        self.author = author
        self.magazine = magazine
        self.title = title
        
class Author:
    all = []
    def __init__(self, name):
        # verify the author name propertites
        if not isinstance(name, str):
            return "Name must be a string"
        if len(name) == 0:
            return "Name must be longer than 0 characters."
        self.name = name
        Author.all.append(self)
    
    def name(self):
        return self._name

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

    def articles(self):
        pass

    def contributors(self):
        pass

    def article_titles(self):
        pass

    def contributing_authors(self):
        pass
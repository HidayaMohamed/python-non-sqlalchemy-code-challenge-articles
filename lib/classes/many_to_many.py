class Article:
    # keep track of every author created.
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
            raise TypeError("Name must be a string") 
        if len(name) == 0:
            raise ValueError("Name must be longer than 0 characters.")
        self.name = name
        Author.all.append(self)
    
    def name(self):
        # Author is now read only / cannot be changed.
        return self._name

    def articles(self):
        # Return all articles written by this author.
        return [a for a in Article.all if a.author is self]

    def magazines(self):
        # Return a list of magazines this author contributed to. 
        return list({a.magazine for a in self.articles()})

    def add_article(self, magazine, title):
        # Create a new article for this author.
        return Article(self, magazine, title)
    
    def topic_areas(self):
        # Return a unique list of categores of magazines this author wrote for.
        mags= self.magazines()
        if not mags :
            return None
        else :
            return list({m.category for m in mags})

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
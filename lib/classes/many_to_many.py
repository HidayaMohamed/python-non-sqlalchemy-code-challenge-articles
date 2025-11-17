class Article:
    # keep track of every article created.
    all= []
    def __init__(self, author, magazine, title):
         # Validate title
        if not isinstance(title, str):
            raise TypeError("Title must be a string.")
        if not (5 <= len(title) <= 50):
            raise ValueError("Title must be between 5 and 50 characters.")

        self._title = title   # title is read-only

        # Validate author
        if not isinstance(author, Author):
            raise TypeError("Author must be an Author instance.")

        # Validate magazine
        if not isinstance(magazine, Magazine):
            raise TypeError("Magazine must be a Magazine instance.")

        # Use setters
        
        self.author = author
        self.magazine = magazine
        Article.all.append(self)
        self.title = title
        
        
class Author:
    all = []
    def __init__(self, name):
        # verify the author name propertites
        if not isinstance(name, str):
            raise TypeError("Name must be a string.") 
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
    # Track all magazines
    def __init__(self, name, category):
        # check if name is a tring, between 2 and 16 characters.
        if not isinstance (name, str):
            raise TypeError("Name must be a string.")
        if not (2 <= len(name) <= 16):
            raise ValueError("Name must be between 2 and 16 characters.")
        # check if the category is a string and longer than 0 characters.
        if not isinstance (category, str):
            raise TypeError ("Category must be a string.")
        if len(category) == 0:
            raise ValueError("Category must be longer than 0 characters.")
        self.name = name
        self.category = category
        Magazine.all.append(self)

    def articles(self):
        return [a for a in Article.all if a.magazine == self]

    def contributors(self):
        return list({a.author for a in self.articles()})

    def article_titles(self):
        arts = self.articles()
        if not arts:
            return None
        return [a.title for a in arts]

    def contributing_authors(self):
         """Authors with more than 2 articles"""
         counts = {}

         for a in self.articles():
            counts[a.author] = counts.get(a.author, 0) + 1

         many = [author for author, count in counts.items() if count > 2]
         return many if many else None
    
    def top_publisher(cls):
        """Magazine with most articles."""
        if not Article.all:
            return None

        counts = {mag: 0 for mag in cls.all}
        for a in Article.all:
            counts[a.magazine] += 1

        top = max(counts, key=lambda m: counts[m])
        return top if counts[top] > 0 else None
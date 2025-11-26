class Article:
    # List of all article instances
    all = []

    def __init__(self, author, magazine, title):
        
        self.author = author
        self.magazine = magazine
        self.title = title

        Article.all.append(self)

    
    @property
    def title(self):
        return self._title
    # sets validation for title.
    @title.setter
    def title(self, value):
        # Title cannot change once set
        if hasattr(self, "_title"):
            raise Exception("Title cannot change once set")

        if not isinstance(value, str):
            raise TypeError("Title must be a string")

        if len(value) < 5 or len(value) > 50:
            raise ValueError("Title must be between 5 and 50 characters")

        self._title = value

    
    @property
    def author(self):
        return self._author

    # sets validation for author
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise TypeError("Author must be an Author instance")

        self._author = value

    # sets property and validation for magazine
    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise TypeError("Magazine must be a Magazine instance")

        self._magazine = value


class Author:
    def __init__(self, name):
        self.name = name

    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        # name cannot change after first setting
        if hasattr(self, "_name"):
            raise Exception("Author name cannot be changed")

        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        if len(value) == 0:
            raise ValueError("Name must be longer than 0 characters")

        self._name = value

    # instance method
    #Return all Article instances written by this author.
    def articles(self):
        result = []
        for article in Article.all:
            if article.author is self:
                result.append(article)
        return result

    # Return a unique list of magazines this author has written for.
    def magazines(self):
        mags = []
        for article in self.articles():
            if article.magazine not in mags:
                mags.append(article.magazine)
        return mags


    # Create a new article written by this author.
    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    # Return unique list of categories of the magazines the author writes for.
    def topic_areas(self):
        mags = self.magazines()
        if len(mags) == 0:
            return None

        categories = []
        for mag in mags:
            if mag.category not in categories:
                categories.append(mag.category)

        return categories


class Magazine:
    # list of all magazines
    all = []

    def __init__(self, name, category):
        self.name = name
        self.category = category
        Magazine.all.append(self)

    # sets property for magazine name
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Name must be a string")

        if len(value) < 2 or len(value) > 16:
            raise ValueError("Name must be 2–16 characters")

        self._name = value

    # sets property and setter validation for category
    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")

        if len(value) == 0:
            raise ValueError("Category must be at least 1 character long")

        self._category = value

    # instance method
    # Return all articles written for this magazine.
    def articles(self):
        result = []
        for article in Article.all:
            if article.magazine is self:
                result.append(article)
        return result

    # instance method 
    # Return unique list of authors who have written for this magazine.
    def contributors(self):
        authors = []
        for article in self.articles():
            if article.author not in authors:
                authors.append(article.author)
        return authors
    
    # Return list of article titles, or None if no articles.
    def article_titles(self):
        arts = self.articles()
        if len(arts) == 0:
            return None
        return [article.title for article in arts]


      
        # Return a list of authors who have written more than 2 articles
        # for this magazine.
        
    def contributing_authors(self):
        counts = {}

        for article in self.articles():
            author = article.author
            counts[author] = counts.get(author, 0) + 1

        result = []
        for author, count in counts.items():
            if count > 2:
                result.append(author)

        return result if result else None

    # classmethod for the top publisher 
     
        # Return magazine with most articles.
        # Return None if no articles exist.
        
    @classmethod
    def top_publisher(cls):
        if len(Article.all) == 0:
            return None
        if len(cls.all) == 0:
            return None

        # count articles per magazine
        counts = {}
        for mag in cls.all:
            counts[mag] = 0

        for article in Article.all:
            counts[article.magazine] += 1

        # return magazine with highest count
        return max(counts, key=counts.get)

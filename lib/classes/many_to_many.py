class Article:
    # Class attribute to store all instances of Article
    all = []

    def __init__(self, author, magazine, title):
        # Initialize Article with an author, magazine, and title
        self.author = author
        self.magazine = magazine
        self.title = title
        # Append the newly created Article to the class attribute 'all'
        Article.all.append(self)

    @property
    def title(self):
        # Getter for the title attribute
        return self._title
    
    @title.setter
    def title(self, new_title):
        # Title setter with validation
        # Once set, the title cannot be changed
        if hasattr(self, "title"):
            AttributeError("Title cannot be changed")
        else:
            if isinstance(new_title, str):
                if 5 <= len(new_title) <= 50:
                    self._title = new_title
                else:
                    # Title must be between 5 and 50 characters
                    ValueError("Title must be between 5 and 50 characters")
            else:
                # Title must be a string
                TypeError("Title must be a string")
            
    @property
    def author(self):
        # Getter for the author attribute
        return self._author
    
    @author.setter
    def author(self, new_author):
        # Author setter with validation
        # Must be an instance of the Author class
        if isinstance(new_author, Author):
            self._author = new_author
        else:
            TypeError("Author must be an instance of Author")
        
    @property
    def magazine(self):
        # Getter for the magazine attribute
        return self._magazine
    
    @magazine.setter
    def magazine(self, new_magazine):
        # Magazine setter with validation
        # Must be an instance of the Magazine class
        if isinstance(new_magazine, Magazine):
            self._magazine = new_magazine
        else:
            TypeError("Magazine must be an instance of Magazine")


class Author:
    def __init__(self, name):
        # Initialize Author with a name
        self.name = name

    @property
    def name(self):
        # Getter for the name attribute
        return self._name

    @name.setter
    def name(self, new_name):
        # Name setter with validation
        # Once set, the name cannot be changed
        if hasattr(self, "name"):
            AttributeError("Name cannot be changed")
        else:
            if isinstance(new_name, str):
                if len(new_name):
                    self._name = new_name
                else:
                    # Name must be longer than 0 characters
                    ValueError("Name must be longer than 0 characters")
            else:
                # Name must be a string
                TypeError("Name must be a string")

    def articles(self):
        # Returns a list of all articles by this author
        return [article for article in Article.all if self == article.author]
    
    def magazines(self):
        # Returns a list of unique magazines the author has written for
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        # Creates a new article and associates it with this author and the given magazine
        return Article(self, magazine, title)

    def topic_areas(self):
        # Returns a list of unique topic areas covered by the author
        topic_areas = list({magazine.category for magazine in self.magazines()})
        # Returns None if no topic areas are found
        if topic_areas:
            return topic_areas
        else:
            return None


class Magazine:
    def __init__(self, name, category):
        # Initialize Magazine with a name and category
        self.name = name
        self.category = category

    @property
    def name(self):
        # Getter for the name attribute
        return self._name

    @name.setter
    def name(self, new_name):
        # Name setter with validation
        # Name must be between 2 and 16 characters
        if isinstance(new_name, str):
            if 2 <= len(new_name) <= 16:
                self._name = new_name
            else: 
                ValueError("Name must be between 2 and 16 characters")
        else:
            TypeError("Name must be a string")   
        
    @property
    def category(self):
        # Getter for the category attribute
        return self._category

    @category.setter
    def category(self, new_category):
        # Category setter with validation
        # Category must be longer than 0 characters
        if isinstance(new_category, str):
            if len(new_category):
                self._category = new_category
            else:
                ValueError("Category must be longer than 0 characters")
        else:
            TypeError("Category must be a string")   

    def articles(self):
        # Returns a list of all articles published in this magazine
        return [article for article in Article.all if self == article.magazine]

    def contributors(self):
        # Returns a list of unique authors who have contributed to this magazine
        return list({article.author for article in self.articles()})

    def article_titles(self):
        # Returns a list of article titles published in this magazine
        article_titles = [magazine.title for magazine in self.articles()]
        # Returns None if no article titles are found
        if article_titles:
            return article_titles
        else:
            return None

    def contributing_authors(self):
        # Returns a list of authors who have written more than one article for this magazine
        authors = {}
        list_of_authors = []

        # Count the number of articles each author has written for this magazine
        for article in self.articles():
            if article.author in authors:
                authors[article.author] += 1
            else:
                authors[article.author] = 1  
        
        # Add authors to the list if they have contributed more than one article
        for author in authors:
            if authors[author] >= 2:
                list_of_authors.append(author) 
                  
        # Returns None if no contributing authors are found
        if (list_of_authors):
            return list_of_authors
        else:
            return None

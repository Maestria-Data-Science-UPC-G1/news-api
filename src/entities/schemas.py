class Link:
    def __init__(self, source, target, value):
        self.source = source
        self.target = target
        self.value = value

    def __dict__(self):
        return {
            'source': self.source,
            'target': self.target,
            'value': self.value
        }

class Node:
    def __init__(self, id, title, content, url, author, description, published_at, group, sentiment):
        self.id = id
        self.title = title
        self.content = content
        self.url = url
        self.author = author
        self.description = description
        self.published_at = published_at
        self.group = group
        self.sentiment = sentiment

    def __dict__(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'url': self.url,
            'author': self.author,
            'description': self.description,
            'published_at': self.published_at,
            'group': self.group,
            'sentiment': self.sentiment
        }
    
class SimilarNode:
    def __init__(self, id, url):
        self.id = id
        self.url = url

    def __dict__(self):
        return {
            'id': self.id,
            'url': self.url
        }
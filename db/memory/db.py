from utils.url import URLRelation

class MemoryDB:
    def __init__(self):
        self.urls = {}

    def save(self, url_relation: URLRelation):
        self.urls[url_relation.code] = url_relation.url

    def find(self, code):
        return self.urls.get(code)

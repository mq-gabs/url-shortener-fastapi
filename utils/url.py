from .code import gen_code
import os

class URLRelation:
    def __init__(self, url):
        self.url = url
        self.code = gen_code()
        self.short_url = os.environ.get("HOST")  + "/c/" + self.code
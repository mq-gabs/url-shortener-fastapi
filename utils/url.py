from .code import gen_code

class URLRelation:
    def __init__(self, url, host):
        self.url = url
        self.code = gen_code()
        self.short_url = "https://" + host + "/c/" + self.code
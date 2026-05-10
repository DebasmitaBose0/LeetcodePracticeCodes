import random
import string

class Codec:
    def __init__(self):
        self.url_map = {}
        # Characters allowed in the short URL: a-z, A-Z, 0-9
        self.chars = string.ascii_letters + string.digits

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL."""
        # Generate a unique 6-character code
        while True:
            code = "".join(random.choices(self.chars, k=6))
            if code not in self.url_map:
                break
        
        self.url_map[code] = longUrl
        return "http://tinyurl.com/" + code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL."""
        # Extract the code from the end of the URL
        code = shortUrl.split('/')[-1]
        return self.url_map.get(code)
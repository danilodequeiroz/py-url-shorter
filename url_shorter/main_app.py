import  base62
from url_shorter.url_shorter_base_64 import UrlShorterBase64


def main():
    url_shorter = UrlShorterBase64()
    url_shorter.long_url = "https://google.com"
    url_shorter.short_url = "https://goo.gl"
    print(f"long url {url_shorter.long_url}")
    print(f"short url {url_shorter.short_url}")
    print("short url: {} long url: {}".format(url_shorter.short_url, url_shorter.long_url) )


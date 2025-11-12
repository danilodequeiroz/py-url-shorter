class UrlShorterBase64:
    long_url = ""
    short_url = ""
    created_at = ""

    def shorturl(self):
        return self.short_url


    def longurl(self):
        return self.long_url
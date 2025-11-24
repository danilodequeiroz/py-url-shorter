class ShortUrl:

    def __init__(self, _id : int,short_url, long_url, created_at,updated_at):
        self.id = _id
        self.short_url = short_url
        self.long_url = long_url
        self.created_at = created_at
        self.updated_at = updated_at

    def primary_key(self):
        return self.id
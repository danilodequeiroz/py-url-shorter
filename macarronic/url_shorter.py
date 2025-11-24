from sqids import Sqids

from clean.domain.model.short_url import ShortUrl
from macarronic.get_last_url import get_last_id

class UrlShorter:

    def shorturl(long_url:str):
        short_url = ShortUrl(
            long_url=long_url,
        )
        sqids = Sqids()
        short_url.short_url = sqids.encode(numbers = [get_last_id()])

        return short_url
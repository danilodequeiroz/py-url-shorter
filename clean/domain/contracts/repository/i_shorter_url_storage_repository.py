from abc import abstractmethod


class ShorterUrlStorageRepositoryInterface:

    @abstractmethod
    def insert_short_url(self, short_url : str ) -> bool:
        raise NotImplementedError("Should implement get_short_url()")

    @abstractmethod
    def get_short_url(self, url_id: int) -> str:
        raise NotImplementedError("Should implement get_short_url()")

    @abstractmethod
    def delete_short_url(self, url_id: int) -> str:
        raise NotImplementedError("Should implement delete_short_url()")

    @abstractmethod
    def get_all_short_urls(self, ) -> []:
        raise NotImplementedError("Should implement get_all_short_urls()")
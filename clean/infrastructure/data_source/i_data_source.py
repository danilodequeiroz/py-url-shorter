from abc import abstractmethod
from typing import List

class DataSourceInterface:

    @abstractmethod
    def save(self, item_to_save : object) -> bool:
        raise NotImplementedError("Should implement print_method_name()")

    @abstractmethod
    def delete_by_object(self, item_to_delete:object) -> bool:
        raise NotImplementedError("Should implement print_method_name()")

    @abstractmethod
    def delete_by_id(self, item_id_to_delete: str) -> bool:
        raise NotImplementedError("Should implement print_method_name()")

    @abstractmethod
    def get(self, item_id:str) -> object:
        raise NotImplementedError("Should implement print_method_name()")

    @abstractmethod
    def get_all(self) -> List[object]:
        raise NotImplementedError("Should implement print_method_name()")

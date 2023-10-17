from typing import TypeVar, Generic

T = TypeVar('T')


class Db(Generic[T]):
    def __init__(self):
        self.__items: list[T] = []

    def get_by_field(self, field: str, value: str | int) -> T | None:
        for item in self.__items:
            if getattr(item, field) == value:
                return item
        return None

    def fetch(self) -> list[T]:
        return self.__items

    def insert(self, item: T):
        self.__items.append(item)

    def extend(self, items: list[T]):
        self.__items.extend(items)

    def remove(self, item: T):
        if item in self.__items:
            self.__items.remove(item)

    def update(self, item: T, new_item: T):
        if item in self.__items:
            self.__items[self.__items.index(item)] = new_item

    def __del__(self):
        # Close database connection
        self.__items = []

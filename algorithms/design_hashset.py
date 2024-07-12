# https://leetcode.com/problems/design-hashset/description/


class MyHashSet:

    def __init__(self):
        self.table: list[int] = []

    def add(self, key: int) -> None:
        if key not in self.table:
            self.table.append(key)

    def remove(self, key: int) -> None:
        if key in self.table:
            self.table.remove(key)

    def contains(self, key: int) -> bool:
        return key in self.table

# https://leetcode.com/problems/design-hashmap/description/


class MyHashMap:

    def __init__(self):
        self.table: list[None | int] = [None]*1000001

    def put(self, key: int, value: int) -> None:
        self.table[key] = value

    def get(self, key: int) -> int:
        res = self.table[key]
        return res if res is not None else -1

    def remove(self, key: int) -> None:
        self.table[key] = None


m = MyHashMap()
m.put(1, 10)
m.put(2, 20)
print(m.get(1))
m.remove(1)
print(m.get(1))

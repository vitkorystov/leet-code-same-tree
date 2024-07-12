# https://leetcode.com/problems/design-linked-list/


class MyLinkedList:

    def __init__(self):
        self.l = []

    def get(self, index: int) -> int:
        if index < len(self.l):
            return self.l[index]
        return -1

    def addAtHead(self, val: int) -> None:
        temp = [val]
        temp.extend(self.l)
        self.l = temp

    def addAtTail(self, val: int) -> None:
        self.l.append(val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index <= len(self.l):
            left = self.l[:index]
            right = self.l[index:]
            left.append(val)
            left.extend(right)
            self.l = left

    def deleteAtIndex(self, index: int) -> None:
        if index < len(self.l):
            self.l.pop(index)


m = MyLinkedList()
m.addAtHead(7)
m.addAtHead(2)
m.addAtHead(1)
m.addAtIndex(3, 0)
print(m.l)  # [1, 2, 7, 0]

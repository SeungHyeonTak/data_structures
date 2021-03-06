# ArrayQueue
"""
연산 복잡도
size - O(1)
isEmpty - O(1)
enqueue - O(1)
dequeue - O(n) - queue의 길이가 길어지면 길어지는 만큼 그에 비례해서 오래걸리는 복잡도를 가지는 연산
peek - O(1)
"""


# class Node:
#     def __init__(self, item):
#         self.data = item
#         self.next = None
#         self.prev = None
#
#
# class DoubleLinkedList:
#     def __init__(self):
#         self.head = Node(None)
#         self.tail = Node(None)
#         self.head.prev = None
#         self.head.next = self.tail
#         self.tail.prev = self.head
#         self.tail.next = None
#         self.count = 0
#
#     def getAt(self, pos):
#         if pos < 0 or pos > self.count:
#             return None
#
#         i = 0
#         curr = self.head
#         while i < pos:
#             curr = curr.next
#             i += 1
#
#         return curr
#
#     def traverse(self):
#         answer = []
#         curr = self.head
#         while curr.next.next:
#             curr = curr.next
#             answer.append(curr.data)
#
#         return answer
#
#     def reverse(self):
#         answer = []
#         curr = self.tail
#         while curr.prev.prev:
#             curr = curr.prev
#             answer.append(curr.data)
#
#         return answer
#
#     def insertAt(self, pos, newnode):
#         if pos < 0 or pos > self.count + 1:
#             return False
#
#         prev = self.getAt(pos - 1)
#         return self.insertAfter(prev, newnode)
#
#     def insertAfter(self, prev, newnode):
#         next = prev.next
#         prev.next = newnode
#         newnode.next = next
#         next.prev = newnode
#         newnode.prev = prev
#         self.count += 1
#         return True
#
#     def popAt(self, pos):
#         if pos < 0 or pos > self.count:
#             return None
#
#         prev = self.getAt(pos - 1)
#         return self.popAfter(prev)
#
#     def popAfter(self, prev):
#         curr = prev.next
#         prev.next = curr.next
#         curr.next.prev = prev
#         self.count -= 1
#
#         return curr.data
#
#
# class LinkedListQueue:
#     def __init__(self):
#         self.data = DoubleLinkedList()
#
#     def size(self):
#         return self.data.count
#
#     def isEmpty(self):
#         return self.size() == 0
#
#     def enqueue(self, item):
#         node = Node(item)
#         self.data.insertAt(self.size() + 1, node)
#
#     def dequeue(self):
#         return self.data.popAt(1)
#
#     def peek(self):
#         return self.data.getAt(1).data
#
#
# if __name__ == "__main__":
#     Q = LinkedListQueue()
#     Q.enqueue(11)
#     Q.enqueue(22)
#     Q.enqueue(33)
#     Q.enqueue(44)
#
#     print(Q.data.traverse())
#     Q.dequeue()
#     print(Q.data.traverse())
#     print(Q.data.getAt(1).data)
#     print(Q.data.count)

class ArrayQueue:
    def __init__(self):
        self.data = []  # 빈 큐 초기화

    def isEmpty(self):
        return self.size() == 0  # 큐가 비어있는지 반환

    def enqueue(self, item):
        self.data.append(item)  # 데이터 원소 추가

    def dequeue(self):  # 시간 복잡도 O(n) 이다 n에 비례하는 시간이 걸린다.
        return self.data.pop()  # 데이터 원소 삭제

    def peek(self):
        return self.data[0]


if __name__ == "__main__":
    Q = ArrayQueue()
    Q.enqueue(1)
    Q.enqueue(2)
    Q.enqueue(3)

    print(Q.data)

    print(Q.dequeue())
    print(Q.data)

    
    
    


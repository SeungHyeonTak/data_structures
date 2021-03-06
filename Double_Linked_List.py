class Node:
    def __init__(self, item):
        self.data = item
        self.next = None
        self.prev = None


class DoubleLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.tail = Node(None)
        self.head.next = self.tail
        self.head.prev = None
        self.tail.next = None
        self.tail.prev = self.head
        self.count = 0

    # 순방향
    def traverse(self):
        answer = []
        curr = self.head
        while curr.next.next:
            curr = curr.next
            answer.append(curr.data)

        return answer

    # 역방향
    def reverse(self):
        answer = []
        curr = self.tail
        while curr.prev.prev:
            curr = curr.prev
            answer.append(curr.data)

        return answer

    # n번째 원소 찾기 divide & conquer 사용 (이유 : list의 길이가 얼마나 늘어날지 모르기 때문에)
    def get(self, pos):
        if pos < 0 or pos > self.count:
            return None

        if pos > self.count // 2:  # 뒤에서부터 찾기
            i = 0
            curr = self.tail
            while i < self.count - pos + 1:
                curr = curr.prev
                i += 1
        else:  # 앞에서 부터 찾기
            i = 0
            curr = self.head
            while i < pos:
                curr = curr.next
                i += 1

        return curr

    def insertAfter(self, prev, newnode):
        next = prev.next
        newnode.prev = prev
        newnode.next = next
        prev.next = newnode
        next.prev = newnode
        self.count += 1

        return True

    def insertAt(self, pos, newnode):
        if pos < 0 or pos > self.count + 1:
            return False

        prev = self.get(pos - 1)
        return self.insertAfter(prev, newnode)

    # # 이 insertBefore() 메서드에는 두 개의 인자가 주어지는데, next는 어느 node의 앞에 새로운 node를 삽입할지를 지정하고, newNode는 삽입할 새로운 node 입니다.
    # def insertBefore(self, next, newnode):
    #     if next == self.head:
    #         return False
    #
    #     prev = next.prev
    #     newnode.prev = prev
    #     newnode.next = next
    #     prev.next = newnode
    #     next.prev = newnode
    #     self.count += 1
    #     return True

    def popAt(self, pos):
        if pos < 0 or pos > self.count:
            raise IndexError

        prev = self.get(pos - 1)
        return self.popAfter(prev)

    def popAfter(self, prev):
        curr = prev.next
        prev.next = curr.next
        curr.next.prev = prev
        self.count -= 1
        return curr.data

    # 두개의 더블 링크드 리스트 연결
    def concat(self, L):
        prev = self.tail.prev
        next = L.head.next
        prev.next = next
        next.prev = prev
        self.tail = L.tail
        self.count += L.count


if __name__ == "__main__":
    L = DoubleLinkedList()
    L2 = DoubleLinkedList()

    node1 = Node(11)
    node2 = Node(22)
    node3 = Node(33)
    node4 = Node(44)

    node5 = Node(55)
    node6 = Node(66)
    node7 = Node(77)
    node8 = Node(88)

    L.insertAt(1, node1)
    L.insertAt(2, node2)
    L.insertAt(3, node3)
    L.insertAt(4, node4)

    L2.insertAt(1, node5)
    L2.insertAt(2, node6)
    L2.insertAt(3, node7)
    L2.insertAt(4, node8)

    print(L.traverse())
    print(L2.traverse())
    print(L.reverse())
    print(L2.reverse())
    L.concat(L2)
    # L.popAt(4)
    print(L.traverse())
    print(L.count)
    
    

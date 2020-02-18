class Node:
    def __init__(self, item):
        self.data = item
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0

    def get(self, pos):
        if pos <= 0 or pos > self.count:
            return None

        i = 1
        curr = self.head
        while i < pos:
            curr = curr.next
            i += 1
        return curr

    def display(self):
        answer = []

        i = 1
        curr = self.head
        while curr != None:
            answer.append(curr.data)
            curr = curr.next
            i += 1

        return answer

    def add(self, pos, newnode):
        if pos < 1 or self.count + 1 < pos:
            return "ERROR: Not added!!"

        if pos == 1:
            newnode.next = self.head
            self.head = newnode
        else:
            if pos == self.count + 1:
                prev = self.tail
            else:
                prev = self.get(pos - 1)
            newnode.next = prev.next
            prev.next = newnode

        if pos == self.count + 1:
            self.tail = newnode

        self.count += 1
        return True

    def delete(self, pos):
        if pos < 1 or pos > self.count:
            return "Error: Not deleted!!"

        elif pos == 1:
            curr = self.get(pos)  # 첫 노드 이므로 따로 prev(pos-1)을 못찾으므로 pos를 찾고 head를 다음 node로 가리키면 된다.
            self.head = curr.next
            if self.count == 1:  # count 즉, 노드의 길이도 1이면 head tail 모두 None으로 처리
                self.head = None
                self.tail = None
        else:
            prev = self.get(pos - 1)
            curr = prev.next
            if pos == self.count:  # pos와 count가 같으면 맨끝을 나타냄
                self.tail = prev
                prev.next = None
            else:
                prev.next = curr.next
        self.count -= 1
        print(curr.data)
        return curr

    # 두개의 연결 리스트 합치기
    def const(self, L):
        self.tail.next = L.head
        if L.tail:
            self.tail = L.tail
        self.count += L.count


if __name__ == "__main__":
    L1 = LinkedList()
    L2 = LinkedList()

    node1 = Node(11)
    node2 = Node(22)
    node3 = Node(33)

    node4 = Node(44)
    node5 = Node(55)
    node6 = Node(66)

    L1.add(1, node1)
    L1.add(2, node2)
    L1.add(3, node3)

    L2.add(1, node4)
    L2.add(2, node5)
    L2.add(3, node6)

    print(L1.display())
    print(L2.display())

    L1.const(L2)

    print("두개의 연결리스트 합치기")
    print(L1.display())
    
    

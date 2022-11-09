class Node:
    def __init__(self, data=None):
        self.data = data
        self.link = None

    def __str__(self):
        return self.data


class SLinkedList:
    def __init__(self):
        self.head = None

    def printList(self):
        node = self.head
        while node is not None:
            print(node.data, end=' ')
            node = node.link
        print()

    def insertAtBegining(self, newdata):
        newNode = Node(newdata)
        newNode.link = self.head
        self.head = newNode

    def insertAtEnd(self, newdata):
        newNode = Node(newdata)
        if self.head is None:
            self.head = newNode
            return
        node = self.head
        while node.link:
            node = node.link
        node.link = newNode

    def findNode(self, find_data):
        current_node = self.head
        while current_node is not None:
            if current_node.data == find_data:
                return current_node
            current_node = current_node.link
        return None

    def insertBetween(self, preData, newdata):
        newNode = Node(newdata)
        pre = self.findNode(preData)

        if pre:
            newNode.link = pre.link
            pre.link = newNode
        else:
            print(f"Error => {preData} Data not found")

    def deleteNode(self, deleteData):
        delete_node = self.findNode(deleteData)
        if not delete_node:
            print(f"Error => {deleteData} Data not found")
        # 첫 번째 노드 삭제
        elif self.head.data == deleteData:
            temp = self.head
            self.head = self.head.link
            del temp
        else:
            current_node = self.head
            while current_node:
                pre = current_node
                current_node = current_node.link
                if current_node.data == deleteData:
                    pre.link = current_node.link
                    del current_node
                    return

def mergeTwoLists(l1: Node, l2: Node) -> Node:
  # l1과 l2를 비교해 작은값이 l1에 저장되도록 함.
  if (not l1) or (l2 and l1.data > l2.data):
    l1, l2 = l2, l1
  if l1:
    l1.link = mergeTwoLists(l1.link, l2)
  return l1


n1 = SLinkedList()
n2 = SLinkedList()

for i, v in enumerate(range(0, 3)):
  n1.insertAtEnd(i*2+1)
  n2.insertAtEnd((i+1)*2)

n1.printList()
n2.printList()


l3 = SLinkedList()
l3.head = mergeTwoLists(n1.head, n2.head)
l3.printList()


def reverse(node: Node, prev: Node = None):
  if not node:
    return prev
  next, node.link = node.link, prev
  return reverse(next, node)


l4 = SLinkedList()
l4.head = reverse(l3.head)
l4.printList()

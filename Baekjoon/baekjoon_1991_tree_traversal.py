n = int(input())

inputs = []
for _ in range(n):
    inputs.append(input().split())


class Node():
    def __init__(self, item, left, right):
        self.item = item
        self.left = left
        self.right = right

    def __str__(self):
        return f'({self.item}, {self.left}, {self.right})'


def preorder(node):
    if node.item == '.':
        return
    print(node.item, end='')
    preorder(tree[node.left])
    preorder(tree[node.right])


def inorder(node):
    if node.item == '.':
        return
    inorder(tree[node.left])
    print(node.item, end='')
    inorder(tree[node.right])


def postorder(node):
    if node.item == '.':
        return
    postorder(tree[node.left])
    postorder(tree[node.right])
    print(node.item, end='')


tree = {}
for item, left, right in inputs:
    tree[item] = Node(item, left, right)
tree['.'] = Node('.', '.', '.')

# for i in tree:
#     print(tree[i])

preorder(tree['A'])
print()
inorder(tree['A'])
print()
postorder(tree['A'])
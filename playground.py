import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline


class Node:
    left = None
    right = None
    value = None


def preorder(node):
    if node is None:
        return
    print(node.value, end="")
    preorder(node.left)
    preorder(node.right)


def inorder(node):
    if node is None:
        return
    inorder(node.left)
    print(node.value, end="")
    inorder(node.right)


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.value, end="")


n = int(input().strip())
nodes = {}
for i in range(n):
    current, left, right = input().strip().split()
    current_node = nodes[current] if current in nodes else Node()

    if left == ".":
        left_node = None
    else:
        left_node = nodes[left] if left in nodes else Node()
        left_node.value = left

    if right == ".":
        right_node = None
    else:
        right_node = nodes[right] if right in nodes else Node()

    current_node.value = current
    current_node.left = left_node
    current_node.right = right_node

    nodes[current] = current_node
    nodes[right] = right_node
    nodes[left] = left_node

preorder(nodes["A"])
print()
inorder(nodes["A"])
print()
postorder(nodes["A"])

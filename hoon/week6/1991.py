# 트리 순회 / 실버1
# 트리 순회를 위한 함수들
import sys
input = sys.stdin.readline
def preorder(node): # 전위
    if node == '.':
        return ''
    left, right = tree[node]
    return node + preorder(left) + preorder(right)

def inorder(node): # 중위
    if node == '.':
        return ''
    left, right = tree[node]
    return inorder(left) + node + inorder(right)

def postorder(node): # 후위
    if node == '.':
        return ''
    left, right = tree[node]
    return postorder(left) + postorder(right) + node
n = int(input())
tree = {}
for _ in range(n):
    parent, left, right = input().split()
    tree[parent] = [left, right]
print(preorder('A'))
print(inorder('A'))
print(postorder('A'))
# -*- coding: utf-8 -*-
# 트리를 구성하는 모든 노드의 x, y 좌표 값은 정수이다.
# 모든 노드는 서로 다른 x값을 가진다.
# 같은 레벨(level)에 있는 노드는 같은 y 좌표를 가진다.
# 자식 노드의 y 값은 항상 부모 노드보다 작다.
# 임의의 노드 V의 왼쪽 서브 트리(left subtree)에 있는 모든 노드의 x값은 V의 x값보다 작다.
# 임의의 노드 V의 오른쪽 서브 트리(right subtree)에 있는 모든 노드의 x값은 V의 x값보다 크다.
# 전위 순회, 후위 순회한 결과를 2차원 배열에 순서대로 담아 return

import sys
from collections import deque

class Node:
    def __init__(self, element):
        self.element = element
        self.left = None
        self.right = None

def preorder(now):
    global prelist

    if now == None: return

    prelist.append(now.element[0])
    preorder(now.left)
    preorder(now.right)
    return

def postorder(now):
    global postlist

    if now == None: return

    postorder(now.left)
    postorder(now.right)
    postlist.append(now.element[0])
    return

def solution(nodeinfo):

    global prelist
    global postlist
    sys.setrecursionlimit(10 ** 6)

    for i in range(0,len(nodeinfo)):
        nodeinfo[i] = [i+1, nodeinfo[i][0], nodeinfo[i][1]]

    sort_node = list(sorted(nodeinfo, key=lambda x: (-x[2],x[1])))
    tree = deque(sort_node)

    head = Node(tree.popleft())
    for _ in range(len(nodeinfo)-1):
        x = tree.popleft()
        newNode = Node(x)
        temp = head
        while True:
            if newNode.element[1] < temp.element[1]:
                if temp.left == None:
                    temp.left = newNode
                    break
                else:
                    temp = temp.left
            else:
                if temp.right == None:
                    temp.right = newNode
                    break
                else:
                    temp = temp.right

    prelist = []
    postlist = []
    preorder(head)
    postorder(head)
    return [prelist,postlist]

nodeinfo = [[1,6]]
print(solution(nodeinfo))

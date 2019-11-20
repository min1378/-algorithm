import sys
sys.stdin = open('1231.txt', 'r')
class Node(object):
    def __init__(self, val):
        self.val = val  # 자신이 관리하는 값
        self.left = None
        self.right = None


class Tree:  # Tree(object)
    def __init__(self):  # 초기화 함수
        self.root = None  # 트리는 루트노드의 필수

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            self._add(val, self.root)  # 재귀적인 저장 함수

    def _add(self, val, node):
        if node.val > val:  # val 은 저장하려는 숫자, 작으면 왼쪽, 크면 오른쪽.
            if node.left is None:
                node.left = Node(val)
            else:  # left 에 node 가 있으면 그 아래에 저장
                self._add(val, node.left)
        else:
            if node.right is None:
                node.right = Node(val)
            else:
                self._add(val, node.right)

    def printAll(self):
        if self.root is None:
            return
        self._print(self.root)

    def _print(self, node):
        if node is not None:
            print(node.val)  # 자기자신출력
            self._print(node.left)
            self._print(node.right)

    def find(self, key):
        return self._find(self.root, key)

    def _find(self, node, key):
        if node is None:
            return False
        if node.val == key:
            return True
        if node.val > key:
            return self._find(node.left, key)
        return self._find(node.right, key)



TC = int(input())
for test_case in range(1, TC+1):
    N = int(input())
    t = Tree()
    s = [40, 4, 34, 35, 14, 55, 48]
    for i in range(len(s)):
        t.add(s[i])  # 숫자추가
    t.printAll()  # 전체저장값 출력하기. 전위, 중위, 후위검색
    print('t.find(34)', t.find(34))
    print('t.find(44)', t.find(44))
#Given a binary tree t and an integer s, determine whether there is a root to leaf path in t such that the sum of vertex values equals s.
# Binary trees are already defined with this interface:
class Tree(object):
  def __init__(self, x):
    self.value = x
    self.left = None
    self.right = None


def solution(t, s):
    print(s)
    if t is None:
        return s == 0
    s = s - t.value
    if t.left is None and t.right is None:
        return s == 0
    elif t.left is not None and t.right is not None:
        return solution(t.left, s) or solution(t.right, s)
    elif t.left is not None and t.right is None:
        return solution(t.left, s)
    elif t.left is None and t.right is not None:
        return solution(t.right, s)


def main():
    s = 7
    tree1 = Tree(4)
    tree1.left = Tree(1)
    tree1.right = Tree(3)
    tree1.left.left = Tree(-2)
    tree1.left.left.right = Tree(3)
    tree1.right.left  = Tree(1)
    tree1.right.right = Tree(2)
    tree1.right.right.left = Tree(-2)
    tree1.right.right.right = Tree(-3)
    assert solution(tree1, 7)
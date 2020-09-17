class Solution():
    class BST:
        def __init__(self, value):
            self.value = value
            self.left = None
            self.right = None

# Recursive solution

    def findClosestValueInBst(tree, target):
        return bstHelperFunction(tree, target, float('inf'))

    def bstHelperFunction(tree, target, closestValue):
        if tree is None:
            return closestValue

        if abs(target - closestValue) > abs(target - tree.value):
            closestValue = tree.value
        if target < tree.value:
            return bstHelperFunction(tree.left, target, closestValue)
        elif target > tree.value:
            return bstHelperFunction(tree.right, target, closestValue)
        else:
            return closestValue

# Iteration solution for finding closest value to target in binary tree

"""

    def findClosestValueInBst(tree, target):
        return bstHelperFunction( tree, target, float('inf'))

    def bstHelperFunction(tree, target, closestValue):
        while tree is not None:
            if abs(target - closestValue) > abs(target - tree.value):
                closestValue = tree.value
            if target < tree.value:
                return bstHelperFunction(tree.left, target, closestValue)
            elif target > tree.value:
                return bstHelperFunction(tree.right, target, closestValue)
            else:
                return closestValue

"""





# This file is initialized with a code version of this
# question's sample test case. Feel free to add, edit,
# or remove test cases in this file as you see fit!

"""
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TestProgram(unittest.TestCase):
    def test_case_1(self):
        root = BST(10)
        root.left = BST(5)
        root.left.left = BST(2)
        root.left.left.left = BST(1)
        root.left.right = BST(5)
        root.right = BST(15)
        root.right.left = BST(13)
        root.right.left.right = BST(14)
        root.right.right = BST(22)
        expected = 13
        actual = program.findClosestValueInBst(root, 12)
        self.assertEqual(expected, actual)
"""
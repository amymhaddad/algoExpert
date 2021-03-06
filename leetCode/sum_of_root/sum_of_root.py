"""
https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/
"""


class Solution:
    def sumRootToLeaf(self, root) -> int:
        totals = []
        helper(root, totals, start="")
        return sum(totals)


def helper(root, totals, start):
    if root is None:
        return
    start += str(root.val)
    if root.right is None and root.left is None:
        dec = int(start, 2)
        return totals.append(dec)
    helper(root.left, totals, start)
    helper(root.right, totals, start)


def sumToRoot(root):
    total = 0

    def helper(root, nums):
        nonlocal total
        if not root.right and not root.left:
            nums += str(root.value)
            total += int(nums, 2)

        nums += str(root.value)
        if root.left:
            helper(root.left, nums)
        if root.right:
            helper(root.right, nums)

    helper(root, "")
    return total

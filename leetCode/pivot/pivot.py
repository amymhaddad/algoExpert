"""
https://leetcode.com/problems/find-pivot-index/
"""


def find_pivot(arr):

    for i in range(len(arr)):
        left_sum = sum(arr[:i])
        right_sum = sum(arr[i + 1 :])
        if left_sum == right_sum:
            return i
    return -1

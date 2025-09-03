"""
Given an array of integers nums and an integer k,
find the maximum sum of any contiguous subarray of size k.
"""
from typing import List


class Solution:
    def maxSum(self, nums: List[int], k: int):
        max_sum = 0
        for i in range(k):
            max_sum += nums[i]
        current_sum = max_sum
        for i in range(k, len(nums)):
            current_sum = nums[i] - nums[i - k] + current_sum
            max_sum = max(max_sum, current_sum)
        return max_sum
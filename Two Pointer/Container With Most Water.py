"""
Given an integer input array heights representing the heights of vertical lines

Write a function that returns the maximum area of water that can be contained
by two of the lines (and the x-axis). The function should take in an array of
integers and return an integer.
"""

class Solution:
    def max_area(self, heights):
        left = 0
        right = len(heights) - 1
        # Initialized to zero because area can't be less than zero
        max_area_global = 0

        while left < right:
            # Formula is we need to take the minimum height and multiply it by
            # right - left which gives the x axis difference
            current_area = min(heights[left], heights[right]) * (right - left)
            max_area_global = max(max_area_global, current_area)
            # This condition is because whichever height is smaller
            # is the height that's limiting the area from getting larger
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return max_area_global
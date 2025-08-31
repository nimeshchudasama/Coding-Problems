"""
Write a function to count the number of triplets in an integer array nums that could form the sides of a triangle.
The triplets do not need to be unique.

The key property is a + b > c such that a < b < c
"""
from typing import List

class Solution:
    def triangleNumber(self, heights: List[int]) -> int:
        heights.sort()
        counter = 0

        # Iterate backwards, picking each element as the largest side (c)
        # We stop at i = 2 because we need at least 2 smaller elements (a and b)
        for i in range(len(heights) - 1, 1, -1):
            c = heights[i]
            a_index = 0
            b_index = i - 1

            # Use two pointers to check all pairs (a, b) with indices < i
            while a_index < b_index:
                # Because the array is sorted:
                # If heights[a_index] + heights[b_index] > c,
                # then EVERY element between a_index and b_index-1
                # also forms a valid 'a' with this 'b' and 'c'.
                if heights[a_index] + heights[b_index] > c:
                    counter += b_index - a_index  # count all those pairs at once
                    b_index -= 1  # move b down to check smaller b values
                else:
                    # Otherwise, sum is too small.
                    # Increase a_index to try a larger 'a'.
                    a_index += 1

        return counter

"""
Given an array of integers representing the value of cards, write a function to calculate the maximum score you can achieve by selecting exactly k cards from either the beginning or the end of the array.

For example, if k = 3, then you have the option to select:
    the first three cards,
    the last three cards,
    the first card and the last two cards
    the first two cards and the last card
"""
from typing import List


class Solution:
    def maxScore(self, cards: List[int], k: int):
        total_sum = sum(cards)
        current_score = 0

        for i in range(k):
            current_score += cards[i]

        min_score = current_score
        for i in range(len(cards) - k, len(cards)):
            current_score += cards[i] - cards[i-k]
            min_score = min(min_score, current_score)

        return total_sum - min_score
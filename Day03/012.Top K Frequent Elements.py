#https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
from queue import PriorityQueue
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_counter = Counter(nums)
        common = num_counter.most_common(k)
        answer = []

        for key, value in common:
            answer.append(key)

        return answer
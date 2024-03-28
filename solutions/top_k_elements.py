# https://leetcode.com/submissions/detail/1209528187/

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = Counter(nums)
        return sorted(count, key=count.get, reverse=True)[:k]
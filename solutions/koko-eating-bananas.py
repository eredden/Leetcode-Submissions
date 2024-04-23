# https://leetcode.com/problems/koko-eating-bananas/submissions/1239518927/
# https://leetcode.com/problems/koko-eating-bananas/solutions/4987596/python-solution-explained-binary-search/

import math

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)
        result = right

        while left <= right:
            mid   = (left + right) >> 1
            hours = 0

            for pile in piles:
                hours += math.ceil(pile / mid)

            if hours <= h:
                result = min(result, mid)
                right = mid - 1
            else:
                left = mid + 1
            
        return result
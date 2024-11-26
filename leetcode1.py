"""Module providing a solution to leetcode problem 1."""

from typing import List
import numpy as np

class Solution:
    """Solution class for problem 1."""

    def two_sum_official(self, nums: List[int], target: int) -> List[int]:
        """Offical solution according to video."""
        seen_at = {}
        for i in enumerate(nums):
            curr = nums[i]
            x = target - curr
            if x in seen_at.keys():
                return seen_at[x],i
            seen_at[curr] = i
        return 0,0

    def two_sum_edu(self, nums: List[int], target: int) -> List[int]:
        """My custom solution using arrays."""
        array = np.asarray(nums)
        found = 0
        roll = 0
        first, second = 0,0
        while found == 0:
            roll=roll+1
            sum_array = np.roll(array,roll)
            res = array + sum_array
            itemindex = np.where(res == target)
            if len(itemindex[0]) > 0:
                found = 1
                first = itemindex[0][0].item()
                if len(itemindex[0]) > 1:
                    second = itemindex[0][1].item()
                else:
                    second = itemindex[0][0].item()-roll
                    if second < 0:
                        second = len(nums)-roll
        return first,second

if __name__ == '__main__':
    solution = Solution()
    indexes = solution.two_sum_official([0,4,3,0],0)
    print(indexes)

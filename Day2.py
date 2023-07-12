# https://leetcode.cn/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        for i in range(len(nums)):
            nums[i] = nums[i] ** 2
        return sorted(nums)
#
#
# solve = Solution()
# print(solve.sortedSquares([-4,-1,0,3,10]))


# 双指针
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:



solve = Solution()
print(solve.sortedSquares([-4,-1,0,3,10]))
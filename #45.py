# 45. Jump Game II


class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        jumps = 0
        currEnd = 0
        farthest = 0

        for i in range(len(nums)):
            farthest = max(farthest, nums[i] + i)
            if i == currEnd and i != len(nums) - 1:
                jumps += 1
                currEnd = farthest
        return jumps


# Time Complexity: O(n)
# Space Complexity: O(1)

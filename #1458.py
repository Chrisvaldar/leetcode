# 1438. Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit

from collections import deque


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        if len(nums) == 1:
            return 1
        maxLen = 0
        left = 0
        right = 0

        maxq = deque()
        maxq.append(0)

        minq = deque()
        minq.append(0)

        while right < len(nums) - 1:
            right += 1

            while maxq and nums[maxq[-1]] <= nums[right]:
                maxq.pop()

            while minq and nums[minq[-1]] >= nums[right]:
                minq.pop()

            maxq.append(right)
            minq.append(right)

            while nums[maxq[0]] - nums[minq[0]] > limit:
                left += 1
                if maxq[0] == left - 1:
                    maxq.popleft()
                if minq[0] == left - 1:
                    minq.popleft()
            maxLen = max(maxLen, right - left + 1)
        return maxLen

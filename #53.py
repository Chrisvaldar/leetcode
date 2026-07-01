class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        currSum = nums[0]

        for i in range(1, len(nums)):
            best = max(currSum + nums[i], nums[i])
            currSum = best
            maxSum = max(best, maxSum)
        return maxSum


# Time Complexity: O(n) for the loop
# Space Complexity: O(1)

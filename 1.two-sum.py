#
# @lc app=leetcode id=1 lang=python
#
# [1] Two Sum
#

# @lc code=start
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)): 
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

        #Hashmap O(n) approach given below
        """
        seen = {}
        for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:
        return [seen[complement], i]
        seen[num] = i
        return []
        """

# @lc code=end


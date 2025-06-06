class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum1=0
        count=0
        for i in range(len(nums)):
            sum1=0
            for j in range(i, len(nums)):
                sum1 += nums[j]
                if sum1 == k:
                    count += 1
        return count
        

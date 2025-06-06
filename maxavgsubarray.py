class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        firstsum = sum(nums[:k])
        maxsum=firstsum
        for i in range(k, len(nums)):
            firstsum += nums[i] - nums[i - k]
            if firstsum>maxsum:
                maxsum=firstsum
        return float(maxsum)/k
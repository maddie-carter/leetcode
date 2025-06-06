class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2)) #returns a list of unique elements that appear in both num1 and nums 2 
    #sets function does not contain duplicates in num1 or nums 2 so being the & will join what is in each set that 
    # is similar then the list function makes it a list which is the return type wanted
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        freq_map = Counter(nums) #counts frequency of each number Counter({1: 3, 2: 2, 3: 1}) for 111223
        sorted_items = sorted(freq_map.items(), key=lambda x: x[1],reverse=True) #freq_map.items() returns a list of (number, frequency) pairs.
#key=lambda x: x[1] means: when sorting, use the second value (the frequency) as the key" reverse=True means:Sort from highest frequency to lowest
   
        return [item[0] for item in sorted_items[:k]]
        #Takes the first k items from sorted_items and extracts item[0], which is the number itself
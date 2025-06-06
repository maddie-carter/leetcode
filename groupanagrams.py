from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        anagram_map = defaultdict(list) #create dictionary of unique keys

        for word in strs:
            key = ''.join(sorted(word))  # sort word to get the key
            anagram_map[key].append(word) #add values that match the key or create a new key and start a new list

        return anagram_map.values() #return the list of the values now sorted into each key
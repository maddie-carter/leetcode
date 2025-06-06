class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        chars_in_s = []
        for i in range(len(s)):
            chars_in_s.append(s[i])
        chars_in_t = []
        for j in range(len(t)):
            chars_in_t.append(t[j])
        chars_in_s.sort()
        chars_in_t.sort()
        return chars_in_s == chars_in_t
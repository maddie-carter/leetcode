class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        max_lengths = []
        sum1=0
        for i in range(len(s)):
            seen = set()
            sum1 = 0
            
            for j in range(i, len(s)):
                if s[j] not in seen:
                    seen.add(s[j])
                    sum1 += 1
                else:
                    break
                    
            max_lengths.append(sum1)
        
        return max(max_lengths) if max_lengths else 0

if __name__ == "__main__":
    s = "abcabcbb"
    sol = Solution()
    result = sol.lengthOfLongestSubstring(s)
    print("Result:", result)
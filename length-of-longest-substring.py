class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0

        char_set = set()
        char_set.add(s[0])
        max_len = 1
        
        l = 0
        r = 1
        while r < len(s):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)
            r += 1
            
        return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        hash_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in hash_set:
                hash_set.remove(s[l])
                l += 1
            hash_set.add(s[r])
            print(hash_set)
            res = max(res, len(hash_set)) # or u can do (r - l + 1)
        return res

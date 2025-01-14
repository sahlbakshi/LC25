class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        for i in range(len(s)):
            hash_set = set()
            for j in range(i, len(s)):
                if s[j] in hash_set:
                    break
                hash_set.add(s[j])
            res = max(res, len(hash_set))
        return res

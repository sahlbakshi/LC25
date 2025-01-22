class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashmap_t = {}
        hashmap_s = {}

        for i in range(len(s)):
            hashmap_t[t[i]] = hashmap_t.get(t[i], 0) + 1
            hashmap_s[s[i]] = hashmap_s.get(s[i], 0) + 1
        
        if hashmap_t == hashmap_s:
            return True
        return False
        
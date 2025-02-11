class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """

        if len(p) > len(s):
            return []
        
        hashmap_p = {}
        hashmap_window = {}  

        for i in range(len(p)):
            hashmap_p[p[i]] = hashmap_p.get(p[i], 0) + 1

        l = 0
        r = len(p) - 1
        
        for i in range(r):
            hashmap_window[s[i]] = hashmap_window.get(s[i], 0) + 1

        res = []
        while r < len(s):
            hashmap_window[s[r]] = hashmap_window.get(s[r], 0) + 1

            if hashmap_window == hashmap_p:
                res.append(l)
            
            hashmap_window[s[l]] = hashmap_window.get(s[l], 0) - 1
            if hashmap_window[s[l]] == 0:
                hashmap_window.pop(s[l])
            l += 1
            r += 1
        
        return res
        
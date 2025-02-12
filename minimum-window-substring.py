class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        if len(t) > len(s):
            return ""

        l = 0
        r = 0

        hashmap = {}
        window = {}

        for i in range(len(t)):
            hashmap[t[i]] = hashmap.get(t[i], 0) + 1
        
        need = len(hashmap)
        have = 0
        res = [-1, -1]
        res_len = len(s)

        while r < len(s):
            if s[r] in hashmap:
                window[s[r]] = window.get(s[r], 0) + 1
                if window[s[r]] == hashmap[s[r]]:
                    have += 1
            
            while have == need:
                if s[l] in window:
                    window[s[l]] = window.get(s[l], 0) - 1
                    if window[s[l]] < hashmap[s[l]]:
                        have -= 1
                if (r - l) + 1 <= res_len:
                    res[0] = l
                    res[1] = r
                    res_len = (r - l) + 1
                l += 1
                
            r += 1
        
        if res[0] == -1:
            return ""
        return s[res[0]: res[1]+1]

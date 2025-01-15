class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashset_t = {}
        for char in t:
            hashset_t[char] = hashset_t.get(char, 0) + 1
        
        window = {}
        substring = [-1, -1]
        substring_len = float("inf")

        have = 0
        need = len(hashset_t)

        l = 0
        r = 0

        while r < len(s):
            char = s[r]
            window[char] = window.get(char, 0) + 1

            if char in hashset_t and window[char] == hashset_t[char]:
                have += 1
            
            while have == need:
                if (r - l + 1) < substring_len:
                    substring = [l, r]
                    substring_len = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in hashset_t and window[s[l]] < hashset_t[s[l]]:
                    have -= 1
                l += 1
            r += 1
        
        l, r = substring
        if substring_len == float('inf'): 
            return ""
        return s[l:r + 1] 

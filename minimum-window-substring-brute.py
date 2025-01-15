class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashset_t = {}
        for char in t:
            hashset_t[char] = hashset_t.get(char, 0) + 1

        substring = ""
        min_len = float('inf')

        for i in range(len(s)):
            hashset_substring = {}
            for j in range(i, len(s)):
                hashset_substring[s[j]] = hashset_substring.get(s[j], 0) + 1

                valid = True
                for key in hashset_t:
                    if hashset_substring.get(key, 0) < hashset_t[key]:
                        valid = False
                        break
                
                if valid:
                    if j - i + 1 < min_len:
                        min_len = j - i + 1
                        substring = s[i:j + 1]
        return substring

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq_map = {}
        max_len = 0
        l = 0
        r = 0

        while r < len(s):
            if s[r] in freq_map:
                freq_map[s[r]] += 1
            else:
                freq_map[s[r]] = 1
            
            most_count = 0
            for char in freq_map:
                if freq_map[char] > most_count:
                    most_count = freq_map[char]

            chars_to_be_replaced = (r - l + 1) - most_count
            if chars_to_be_replaced <= k:
                max_len = max((r - l + 1), max_len)
            else:
                freq_map[s[l]] -= 1
                l += 1
            
            r += 1
        
        return max_len

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams_map = {}
        for anagram in strs:
            sorted_anagram = ''.join(sorted(anagram))
            if sorted_anagram not in anagrams_map:
                anagrams_map[sorted_anagram] = []
            anagrams_map[sorted_anagram].append(anagram)
        
        result = []
        # for key in anagrams_map:
        # for key, value in anagrams_map.items():
        # for value in anagrams_map.values():
        for key in anagrams_map:
            result.append(anagrams_map[key])
        
        return result

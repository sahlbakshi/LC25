class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        phone_mapping = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z'],
        }

        res = []
        def helper(i, arr):
            if i == len(digits):
                res.append(arr)
                return
            
            num = digits[i]
            for letter in phone_mapping[num]:
                helper(i+1, arr + [letter])
        
        if digits:
            helper(0, [])
        
        for i in range(len(res)):
            res[i] = ''.join(res[i])
        
        return res
        
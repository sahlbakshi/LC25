class Solution:
    def isValid(self, s: str) -> bool:
        hashset = {'}' : '{', ')': '(', ']':'['}
        stack = []

        for char in s:
            if char not in hashset:
                stack.append(char)
            else:
                if stack == []:
                    return False
                elem = stack.pop()
                if elem != hashset[char]:
                    return False
        return len(stack) == 0

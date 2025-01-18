class Solution:
    def isValid(self, s: str) -> bool:
        char_map = {
            '{' : '}',
            '(' : ')',
            '[' : ']'
        }

        stack = []
        for char in s:
            if char in char_map:
                stack.append(char)
            else:
                if stack == []:
                    return False
                last = stack.pop()
                if char_map[last] != char:
                    return False
        if stack != []: return False
        return True
        
class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            string_len = len(string)
            res += str(string_len) + '#'
            res += string
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        string_len = 0
        string = ''
        i = 0
        while i < len(s):
            if string_len == 0:
                res.append(string)
                string = ''
                num = ''
                while s[i] != '#':
                    num += s[i]
                    i += 1
                string_len = int(num)
            else:
                string += s[i]
                string_len -= 1
            i += 1
        res.append(string)
        res.pop(0)
        return res
        
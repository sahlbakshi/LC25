class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for string in strs:
            string_len = str(len(string))
            res += string_len
            res += '#'
            res += string
        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        s_len = ''

        i = 0
        while i < len(s):
            while s[i] != '#':
                s_len += s[i]
                i += 1

            start = i + 1
            end = i + int(s_len)
            res.append(s[start:end + 1]) # to include the last element
            
            i = end + 1
            s_len = ''
        return res

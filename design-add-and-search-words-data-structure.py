class WordNode:
    def __init__(self):
        self.children = {}
        self.end = False

class WordDictionary:
    def __init__(self):
        self.root = WordNode()

    def addWord(self, word: str) -> None:
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = WordNode()
            curr = curr.children[c]
        curr.end = True

    def search(self, word: str) -> bool:
        word_len = len(word)
        
        def recurse(node, j):
            if j >= word_len:
                return node.end

            char = word[j]
            if char == '.':
                for k in node.children:
                    if recurse(node.children[k], j+1):
                        return True
                return False
            else:
                if char not in node.children:
                    return False
                return recurse(node.children[char], j+1)
        
        return recurse(self.root, 0)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)

class Node:
    __slots__ = 'son','end'
    
    def __init__(self):
        self.son={}
        self.end=False

class Trie:
    def __init__(self):
        self.root=Node()

    def insert(self, word: str) -> None:
        cur=self.root
        for char in word:
            if char not in cur.son:
                cur.son[char]=Node()
            cur=cur.son[char]
        cur.end=True

    def search(self, word: str) -> bool:
        cur=self.root
        for char in word:
            if char not in cur.son:
                return False
            cur=cur.son[char]
        return cur.end

    def startsWith(self, prefix: str) -> bool:
        cur=self.root
        for char in prefix:
            if char not in cur.son:
                return False
            cur=cur.son[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

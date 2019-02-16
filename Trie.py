class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = dict()

class Trie():
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        word = word.lower()
        cur = self.root
        for l in word:
            if l not in cur.children:
                cur.children[l] = TrieNode()
            cur = cur.children[l]
        cur.isEnd = True

    def isPrefix(self, prefix):
        prefix = prefix.lower()
        cur = self.root
        for l in prefix:
            if l not in cur.children:
                return False
            else:
                cur = cur.children[l]
        return True

    def isWord(self, word):
        word = word.lower()
        cur = self.root
        for l in word:
            if l not in cur.children:
                return False
            else:
                cur = cur.children[l]
        return cur.isEnd

if __name__ == '__main__':  
    trie = Trie()

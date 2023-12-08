class TrieNode:
    def __init__(self):
        # TrieNode would have children. Using hashmap as its easy and quick
        self.children = {}
        # TrieNode can be a ending node. So we need a var to keep track of that
        self.endNode = False

class Trie:

    def __init__(self):
        # Here our Trie (prefix tree) would have a root
        self.root = TrieNode()
        

    def insert(self, word: str) -> None:
        # We start at root
        current = self.root

        # We need to iterate through each character of the word
        for character in word:
            # We check if this exists in our Trie or not. If it does not we create a new trienode and add it to our trie
            if character not in current.children:
                current.children[character] = TrieNode()
            # Else we would update the position of current
            current = current.children[character]
        # The final word would be the endNode, thus we set it to true
        current.endNode = True

    def search(self, word: str) -> bool:
        # We start at root
        current = self.root

        # We need to iterate through each character of the word
        for character in word:
            # We check if this character exists. If not, then we return false
            if character not in current.children:
                return False
            current = current.children[character]
        return current.endNode

    def startsWith(self, prefix: str) -> bool:
        # We start at root
        current = self.root

        # We iterate through each of the prefix characters
        for character in prefix:
            # We check if this character exists. If not, then we return false
            if character not in current.children:
                return False
            current = current.children[character]
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

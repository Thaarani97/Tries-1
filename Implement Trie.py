class TrieNode:   
    def __init__(self):
        
        self.isEnd = False
        self.childrens = [None]*26
        
class Trie(object):

    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word): # TC - O(m), where m is the key length., #SC - O(m)
        """
        :type word: str
        :rtype: None
        """
        curr = self.root
        for char in word:
            key = ord(char) - ord('a')
            if curr.childrens[key] == None:
                curr.childrens[key] = TrieNode()
            
            curr = curr.childrens[key]
        curr.isEnd = True
        
    def search(self, word): # TC - O(m), where m is the key length., #SC - O(1)
        """
        :type word: str
        :rtype: bool
        """
        curr = self.root
        for char in word:
            key = ord(char) - ord('a')
            if curr.childrens[key] == None:
                return False
            
            curr = curr.childrens[key]
        return curr.isEnd
        

    def startsWith(self, prefix):# TC - O(m), where m is the key length., #SC - O(1)
        """
        :type prefix: str
        :rtype: bool
        """
        curr = self.root
        for char in prefix:
            key = ord(char) - ord('a')
            if curr.childrens[key] == None:
                 return False
            
            curr = curr.childrens[key]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
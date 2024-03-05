class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_str = ""
        ind = 0
        while ind < len(word1) or ind < len(word2):
            char1 = word1[ind] if ind < len(word1) else ""
            char2 = word2[ind] if ind < len(word2) else ""
            new_str += char1 + char2
            ind += 1
        return new_str
                
        
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new_string = ""
        index = 0
        while index < len(word1) or index < len(word2):
            character1 = word1[index] if index < len(word1) else ""
            character2 = word2[index] if index < len(word2) else ""
            new_string += character1 + character2
            index += 1
        return new_string
                
        
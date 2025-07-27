class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        
        position = word.find(ch)
        return word[:position + 1][::-1] + word[position + 1:]
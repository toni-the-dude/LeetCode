class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        
        if word.lower() == word or word[0] + word[1:].lower() == word or word.upper() == word:
            return True

        return False